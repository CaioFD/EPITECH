import argparse
import datetime
import os
import random
import sys
import time

# ANSI color codes
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

# High scores are always saved next to the program (not in the current folder).
# Once packaged with PyInstaller, __file__ is in a temp folder, so use the executable's folder.
if getattr(sys, "frozen", False):
    APP_DIR = os.path.dirname(sys.executable)
else:
    APP_DIR = os.path.dirname(os.path.abspath(__file__))
SCORE_FILE = os.path.join(APP_DIR, "highscores.txt")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB: refuse bigger files (or /dev/zero...)
MAX_WORD_LEN = 30                 # ignore absurdly long lines / inputs


def error(msg):
    # Errors go to the standard error output
    print(f"Error: {msg}", file=sys.stderr)


def positive_int(value):
    # argparse type: accepts only integers > 0
    try:
        n = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not an integer")
    if n <= 0:
        raise argparse.ArgumentTypeError(f"'{value}' must be greater than 0")
    return n


def get_args():
    parser = argparse.ArgumentParser(description="Hangman game")
    parser.add_argument("file", nargs="?",
                        help="file with one word per line")
    parser.add_argument("-p", "--penalties", type=positive_int, default=12,
                        help="max penalties before losing (default: 12)")
    parser.add_argument("-l", "--length", type=positive_int,
                        help="length of the word to guess")
    parser.add_argument("-t", "--time", type=positive_int,
                        help="time limit in seconds")
    args = parser.parse_args()
    if args.file is None:
        error("missing argument")
        sys.exit(1)
    return args


def load_words(path):
    # Returns the valid words of the file, or raises ValueError with a clear message
    if not os.path.exists(path):
        raise ValueError(f"'{path}' does not exist")
    if not os.path.isfile(path):   # directory, /dev/zero, pipe...
        raise ValueError(f"'{path}' is not a regular file")
    if os.path.getsize(path) > MAX_FILE_SIZE:
        raise ValueError(f"'{path}' is too big")
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except PermissionError:
        raise ValueError(f"no permission to read '{path}'")
    except UnicodeDecodeError:
        raise ValueError(f"'{path}' is not a text file")
    except OSError as e:
        raise ValueError(f"cannot read '{path}' ({e.strerror})")

    # Keep only plain A-Z words (no spaces, digits, accents, empty lines...)
    words = {w.strip().upper() for w in lines}
    words = [w for w in words if w.isascii() and w.isalpha() and len(w) <= MAX_WORD_LEN]
    if not words:
        raise ValueError(f"no valid word in '{path}'")
    return words


def pick_word(words, length):
    if length:
        words = [w for w in words if len(w) == length]
    if not words:
        return None  # no word has the requested length
    return random.choice(words)


def best_score():
    # Returns (attempts, date) of the record, or None if there is no record yet
    best = None
    try:
        with open(SCORE_FILE, encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) != 3 or not parts[2].isdigit():
                    continue  # corrupted line: ignore it
                try:
                    date = datetime.date.fromisoformat(parts[0])
                except ValueError:
                    continue
                attempts = int(parts[2])
                if best is None or attempts < best[0]:
                    best = (attempts, date)
    except (OSError, UnicodeDecodeError):
        pass  # no file yet, or unreadable: act as if there is no record
    return best


def save_score(word, attempts):
    # Saves the game if it beats the record, and returns the message to show
    best = best_score()
    if best and attempts >= best[0]:
        return (f"You guessed '{word}' in {attempts} attempts, "
                f"but the record from {best[1]} is {best[0]} attempts.")
    try:
        with open(SCORE_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.date.today()};{word};{attempts}\n")
    except OSError:
        error("could not save the high score")
    return f"Best ever! You guessed '{word}' in {attempts} attempts."


class Hangman:
    # The game rules only (no print / input), so the pygame version can reuse them

    def __init__(self, word, max_penalties):
        self.word = word
        self.max_penalties = max_penalties
        self.found = set()   # letters guessed that ARE in the word
        self.wrong = set()   # letters guessed that are NOT in the word
        self.penalties = 0
        self.attempts = 0    # valid new guesses (repeats and typos don't count)
        self.word_guessed = False

    def won(self):
        return self.word_guessed or set(self.word) <= self.found

    def lost(self):
        return not self.won() and self.penalties >= self.max_penalties

    def guess(self, text):
        # Plays one guess. Returns (status, message), status is "good", "bad" or "info"
        guess = text.strip().upper()
        if not guess.isascii() or not guess.isalpha():
            return "info", "Please type only letters (A-Z)."
        if len(guess) > MAX_WORD_LEN:
            return "info", "That's way too long."

        if len(guess) == 1:                  # guessing one letter
            if guess in self.found:
                return "info", f"'{guess}' was already found"
            if guess in self.wrong:          # repeated wrong letter: no penalty
                return "info", f"'{guess}' was already tried (no penalty)"
            self.attempts += 1
            if guess in self.word:
                self.found.add(guess)
                return "good", f"Found {self.word.count(guess)} '{guess}'"
            self.wrong.add(guess)
            self.penalties += 1
            return "bad", f"No '{guess}' found"

        self.attempts += 1                   # guessing the full word
        if guess == self.word:
            self.word_guessed = True
            return "good", f"{guess}: correct guess"
        self.penalties += 5
        return "bad", f"{guess}: incorrect guess"


def show(game):
    # Found letters in green, the others hidden as "_"
    hidden = " ".join(GREEN + c + RESET if c in game.found or game.word_guessed else "_"
                      for c in game.word)
    label = "penalty" if game.penalties <= 1 else "penalties"
    print(f"{hidden} / {BLUE}{game.penalties} {label}{RESET}")
    if game.wrong:
        print(f"Wrong letters: {RED}{', '.join(sorted(game.wrong))}{RESET}")


def play(words, args):
    word = pick_word(words, args.length)
    game = Hangman(word, args.penalties)
    colors = {"good": GREEN, "bad": RED, "info": YELLOW}
    start = time.time()
    show(game)

    while True:
        text = input("$> ")

        # The time is only checked after each guess (input() can't be interrupted)
        if args.time and time.time() - start > args.time:
            print(f"{RED}Time's up! The word was {word}{RESET}")
            return

        status, message = game.guess(text)
        print(colors[status] + message + RESET)

        if game.won():
            print(f"{GREEN}{save_score(word, game.attempts)}{RESET}")
            return
        if game.lost():
            print(f"{RED}You lose! The word was {word}{RESET}")
            return
        show(game)


def main():
    args = get_args()
    try:
        words = load_words(args.file)
    except ValueError as e:
        error(e)
        sys.exit(1)
    if pick_word(words, args.length) is None:
        error(f"no word of {args.length} letters in the file")
        sys.exit(1)

    try:
        while True:
            play(words, args)
            if input("Play again? (y/n): ").strip().lower() != "y":
                break
        print("Bye!")
    except (KeyboardInterrupt, EOFError):  # Ctrl+C / Ctrl+D
        print("\nBye!")


if __name__ == "__main__":
    main()