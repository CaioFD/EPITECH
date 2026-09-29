import argparse
import os
import random
import time
from english_words import get_english_words_set

# ANSI color codes
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

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
    # Found letters in green, the others hidden as "_"
    hidden = " ".join(GREEN + c + RESET if c in found else "_" for c in word)
    label = "penalty" if penalties <= 1 else "penalties"
    print(f"{hidden} / {BLUE}{penalties} {label}{RESET}")
    if wrong:
        print(f"Wrong letters: {RED}{', '.join(sorted(wrong))}{RESET}")


def play(args):
    word = pick_word(load_words(args.file), args.length)
    if word is None:
        print(f"{RED}No word matches these options.{RESET}")
        return

    found = set()   # letters guessed that ARE in the word
    wrong = set()   # letters guessed that are NOT in the word
    penalties = 0
    start = time.time()
    show(word, found, wrong, penalties)

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

        if penalties >= args.penalties:
            print(f"{RED}You lose! The word was {word}{RESET}")
            return

        show(word, found, wrong, penalties)


# Options are read once and reused for every new game
args = get_args()
while True:
    play(args)
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Bye!")
        break