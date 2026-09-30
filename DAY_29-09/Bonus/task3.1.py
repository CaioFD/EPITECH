import random
from english_words import get_english_words_set

# ANSI color codes
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

MAX_PENALTIES = 12
BOT_MISTAKE_CHANCE = 0.3   # 30% of the time the bot plays a random letter


def pattern_of(word, found):
    return "".join(c if c in found else "_" for c in word)


def matches(candidate, pattern, tried):
    for c, p in zip(candidate, pattern):
        if p == "_":
            if c in tried:           # a tried letter would already be revealed
                return False
        elif c != p:                 # a revealed letter must be the same
            return False
    return True


def bot_guess(candidates, tried, pattern):
    # Whole word only when just 1 letter is missing (and the bot knows the word)
    if pattern.count("_") == 1 and len(candidates) == 1:
        return candidates[0]
    # Sometimes the bot "makes a mistake" and picks a random untried letter
    untried = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in tried]
    if random.random() < BOT_MISTAKE_CHANCE:
        return random.choice(untried)
    # Otherwise: the untried letter that appears in the most possible words
    counts = {}
    for w in candidates:
        for c in set(w):
            if c not in tried:
                counts[c] = counts.get(c, 0) + 1
    if counts:
        return max(counts, key=counts.get)
    for c in "etaoinshrdlcumwfgypbvkjxqz":   # no candidate left: common letters first
        if c not in tried:
            return c


def ask_guess(tried):
    # Your turn: a new letter or a whole word
    while True:
        guess = input("Your turn $> ").strip().lower()
        if not guess.isalpha():
            print(f"{YELLOW}Please type only letters.{RESET}")
        elif len(guess) == 1 and guess in tried:
            print(f"{YELLOW}'{guess.upper()}' was already tried, choose another.{RESET}")
        else:
            return guess


def show(word, found, tried, penalties):
    hidden = " ".join(GREEN + c.upper() + RESET if c in found else "_" for c in word)
    print(f"\n{hidden}")
    print(f"Penalties -> You: {BLUE}{penalties['You']}{RESET} | Bot: {BLUE}{penalties['Bot']}{RESET}")
    if tried:
        print("Tried letters:", ", ".join(sorted(tried)).upper())


def play(words):
    # One duel on the same secret word, turn by turn; returns the winner
    word = random.choice([w for w in words if 5 <= len(w) <= 8])
    found = set()
    tried = set()                          # letters tried by BOTH players
    penalties = {"You": 0, "Bot": 0}
    candidates = [w for w in words if len(w) == len(word)]
    player = "You"                         # you always start

    while True:
        show(word, found, tried, penalties)
        other = "Bot" if player == "You" else "You"

        if player == "You":
            guess = ask_guess(tried)
        else:
            pattern = pattern_of(word, found)
            candidates = [w for w in candidates if matches(w, pattern, tried)]
            guess = bot_guess(candidates, tried, pattern)
            print(f"Bot plays {BLUE}{guess.upper()}{RESET}")

        if len(guess) == 1:                # a letter
            tried.add(guess)
            if guess in word:
                found.add(guess)
                print(f"{GREEN}{player}: found {word.count(guess)} '{guess.upper()}'{RESET}")
                if set(word) <= found:     # this letter completed the word
                    print(f"{GREEN}{player} completed the word {word.upper()}!{RESET}")
                    return player
            else:
                penalties[player] += 1
                print(f"{RED}{player}: no '{guess.upper()}' (+1 penalty){RESET}")
        elif guess == word:                # a whole word, correct
            print(f"{GREEN}{player} guessed the word {word.upper()}!{RESET}")
            return player
        else:                              # a whole word, wrong
            penalties[player] += 5
            print(f"{RED}{player}: {guess.upper()} is wrong (+5 penalties){RESET}")

        if penalties[player] >= MAX_PENALTIES:
            print(f"{RED}{player} reached {MAX_PENALTIES} penalties! The word was {word.upper()}{RESET}")
            return other

        player = other                     # next turn


words = list(get_english_words_set(["web2"], lower=True, alpha=True))
score = {"You": 0, "Bot": 0}
print("Duel against the bot: same word, one turn each.")
print("Complete the word or guess it before the bot does!")

while True:
    winner = play(words)
    score[winner] += 1
    message = "You win this round!" if winner == "You" else "The bot wins this round!"
    print(f"\n{BLUE}{message}{RESET}  Score -> You {score['You']} x {score['Bot']} Bot")
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Bye!")
        break