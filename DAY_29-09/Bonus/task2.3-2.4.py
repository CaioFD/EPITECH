import argparse
import random
import time
from english_words import get_english_words_set

# ANSI color codes
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

HINT_COST = 2

def get_args():
    # Options
    parser = argparse.ArgumentParser(description="Hangman in the terminal")
    parser.add_argument("-p", "--penalties", type=int, default=12,
                        help="max penalties before losing (default: 12)")
    parser.add_argument("-l", "--length", type=int,
                        help="length of the word to guess")
    parser.add_argument("-f", "--file",
                        help="file with one word per line (use it for a theme)")
    parser.add_argument("-t", "--time", type=int,
                        help="time limit in seconds")
    return parser.parse_args()


def load_words(file):
    # Words from the given file, or from the english-words package if no file
    if file:
        with open(file) as f:
            return [w.strip() for w in f if w.strip().isalpha()]
    return list(get_english_words_set(["web2"], lower=True, alpha=True))


def pick_word(words, length):
    if length:
        words = [w for w in words if len(w) == length]
    if not words:
        return None  # no word has the requested length
    return random.choice(words).upper()


def show(word, found, wrong, penalties):
    hidden = " ".join(GREEN + c + RESET if c in found else "_" for c in word)
    label = "penalty" if penalties <= 1 else "penalties"
    print(f"{hidden} / {BLUE}{penalties} {label}{RESET}")
    if wrong:
        print(f"Wrong letters: {RED}{', '.join(sorted(wrong))}{RESET}")


def give_hint(word, found, penalties, limit):
    # Task 2.3: reveals one missing letter for 2 penalties, returns the new penalties
    missing = [c for c in set(word) if c not in found]
    if not missing:
        print(f"{YELLOW}Hint refused: the word is already revealed.{RESET}")
        return penalties
    if penalties + HINT_COST >= limit:
        print(f"{YELLOW}Hint refused: it would make you lose.{RESET}")
        return penalties
    letter = random.choice(missing)
    found.add(letter)
    print(f"{GREEN}Hint: the word contains '{letter}' (+{HINT_COST} penalties){RESET}")
    return penalties + HINT_COST


def play(args):
    word = pick_word(load_words(args.file), args.length)
    if word is None:
        print(f"{RED}No word matches these options.{RESET}")
        return None                          # no game played: nothing to store

    found = set()   # letters guessed that ARE in the word
    wrong = set()   # letters guessed that are NOT in the word
    penalties = 0
    start = time.time()
    print(f"{BLUE}Type ? for a hint.{RESET}")
    show(word, found, wrong, penalties)

    while True:
        guess = input("$> ").strip().upper()

        # The time is only checked after each guess (input() can't be interrupted)
        if args.time and time.time() - start > args.time:
            print(f"{RED}Time's up! The word was {word}{RESET}")
            return {"word": word, "won": False, "penalties": penalties}

        if guess == "?":                     # Task 2.3: ask for a hint
            penalties = give_hint(word, found, penalties, args.penalties)
        elif not guess.isalpha():
            print(f"{YELLOW}Please type only letters.{RESET}")
            continue
        elif len(guess) == 1:                # guessing one letter
            if guess in found:
                print(f"{YELLOW}'{guess}' was already found{RESET}")
            elif guess in wrong:             # repeated wrong letter: no penalty
                print(f"{YELLOW}'{guess}' was already tried (no penalty){RESET}")
            elif guess in word:
                found.add(guess)
                print(f"{GREEN}Found {word.count(guess)} '{guess}'{RESET}")
            else:
                wrong.add(guess)
                penalties += 1
                print(f"{RED}No '{guess}' found{RESET}")
        else:                                # guessing the full word
            if guess == word:
                print(f"{GREEN}{word}: correct guess - {penalties} penalties{RESET}")
                return {"word": word, "won": True, "penalties": penalties}
            penalties += 5
            print(f"{RED}{guess}: incorrect guess{RESET}")

        # Win: every letter of the word is in the found set
        if set(word) <= found:
            print(f"{GREEN}{word}: You found it! - {penalties} penalties{RESET}")
            return {"word": word, "won": True, "penalties": penalties}

        if penalties >= args.penalties:
            print(f"{RED}You lose! The word was {word}{RESET}")
            return {"word": word, "won": False, "penalties": penalties}

        show(word, found, wrong, penalties)


# Task 2.4: scoreboard functions
def win_rate(history):
    if not history:
        return 0                     # no game played: avoid dividing by zero
    wins = sum(1 for game in history if game["won"])
    return wins / len(history) * 100


def average_penalties_won(history):
    won = [game["penalties"] for game in history if game["won"]]
    if not won:
        return None                  # no game won: no average
    return sum(won) / len(won)


def longest_word_found(history):
    won = [game["word"] for game in history if game["won"]]
    if not won:
        return None
    return max(won, key=len)


def print_stats(history):
    print(f"\nGames played: {len(history)}")
    print(f"Win rate: {win_rate(history):.1f}%")
    average = average_penalties_won(history)
    if average is None:
        print("No game won yet.")
    else:
        print(f"Average penalties on won games: {average:.1f}")
        print(f"Longest word found: {longest_word_found(history)}")


# Options are read once and reused for every new game
args = get_args()
history = []                                 # one dict per game
while True:
    result = play(args)
    if result is not None:
        history.append(result)
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print_stats(history)
        print("Bye!")
        break