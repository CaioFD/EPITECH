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

# Task 3.3: themes and their words
THEMES = {
    "fruits": ["apple", "banana", "cherry", "grape", "lemon", "mango",
               "orange", "peach", "pear", "pineapple", "strawberry", "kiwi"],
    "animals": ["cat", "dog", "horse", "tiger", "zebra", "rabbit", "monkey",
                "giraffe", "dolphin", "penguin", "elephant", "kangaroo"],
    "code": ["python", "function", "variable", "loop", "string", "integer",
             "boolean", "keyboard", "compiler", "recursion", "argument", "module"],
}
# Harder theme = more penalties allowed ("custom" = words from -f, bonus 0)
THEME_BONUS = {"fruits": 0, "animals": 1, "code": 2, "english": 3}

def get_args():
    # Options
    parser = argparse.ArgumentParser(description="Hangman in the terminal")
    parser.add_argument("-p", "--penalties", type=int,
                        help="max penalties before losing (default: depends on theme and word)")
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


def show(word, found, wrong, penalties, theme, limit):
    # Found letters in green, the others hidden as "_"
    hidden = " ".join(GREEN + c + RESET if c in found else "_" for c in word)
    print(f"Theme: {BLUE}{theme}{RESET} | {hidden} / {BLUE}{penalties}/{limit} penalties{RESET}")
    if wrong:
        print(f"Wrong letters: {RED}{', '.join(sorted(wrong))}{RESET}")


def choose_theme():
    names = list(THEMES) + ["english"]
    print("Themes:", ", ".join(names), "or random")
    while True:
        choice = input("Choose a theme: ").strip().lower()
        if choice == "random":
            return random.choice(names)
        if choice in names:
            return choice
        print(f"{YELLOW}Unknown theme.{RESET}")


def theme_words(theme):
    if theme == "english":
        return load_words(None)           
    return THEMES[theme]


def max_penalties(word, theme):
    # Task 3.3 difficulty formula: 8 + half the word length + theme bonus
    return 8 + len(word) // 2 + THEME_BONUS.get(theme, 0)


def play(args):
    if args.file:
        theme = "custom"                     # words from the -f file
        words = load_words(args.file)
    else:
        theme = choose_theme()
        words = theme_words(theme)

    word = pick_word(words, args.length)
    if word is None:
        print(f"{RED}No word matches these options.{RESET}")
        return

    # -p wins if given, otherwise the difficulty formula decides
    limit = args.penalties if args.penalties else max_penalties(word, theme)

    found = set()   # letters guessed that ARE in the word
    wrong = set()   # letters guessed that are NOT in the word
    penalties = 0
    start = time.time()
    show(word, found, wrong, penalties, theme, limit)

    while True:
        guess = input("$> ").strip().upper()

        # The time is only checked after each guess (input() can't be interrupted)
        if args.time and time.time() - start > args.time:
            print(f"{RED}Time's up! The word was {word}{RESET}")
            return

        if not guess.isalpha():
            print(f"{YELLOW}Please type only letters.{RESET}")
            continue

        if len(guess) == 1:              # guessing one letter
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
                return
            penalties += 5
            print(f"{RED}{guess}: incorrect guess{RESET}")

        # Win: every letter of the word is in the found set
        if set(word) <= found:
            print(f"{GREEN}{word}: You found it! - {penalties} penalties{RESET}")
            return

        if penalties >= limit:
            print(f"{RED}You lose! The word was {word}{RESET}")
            return

        show(word, found, wrong, penalties, theme, limit)


# Options are read once and reused for every new game
args = get_args()
while True:
    play(args)
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Bye!")
        break