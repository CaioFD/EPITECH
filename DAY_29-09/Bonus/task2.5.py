# import random

# WORDS = ["python", "banana", "keyboard", "giraffe", "function", "orange",
#          "dolphin", "variable", "penguin", "computer", "hangman", "elephant"]
# MAX_ATTEMPTS = 3


# def shuffle_letters(word):
#     # Fisher-Yates shuffle, done by hand (random.shuffle is not allowed)
#     letters = list(word)
#     for i in range(len(letters) - 1, 0, -1):
#         j = random.randint(0, i)                         # random position from 0 to i
#         letters[i], letters[j] = letters[j], letters[i]  # swap the two letters
#     return "".join(letters)


# def scramble(word):
#     # Shuffle again until the result is different from the original
#     mixed = shuffle_letters(word)
#     while mixed == word:
#         mixed = shuffle_letters(word)
#     return mixed


# def play():
#     word = random.choice(WORDS)
#     print(f"Unscramble this word: {scramble(word).upper()}")
#     attempts = MAX_ATTEMPTS
#     while attempts > 0:
#         guess = input("$> ").strip().lower()
#         if guess == word:
#             print("Correct! Well done.")
#             return
#         attempts -= 1
#         print(f"Wrong! Attempts left: {attempts}")
#     print(f"You lose! The word was {word.upper()}")


# play()



import random
from english_words import get_english_words_set

MAX_ATTEMPTS = 5


def load_words():
    words = get_english_words_set(["web2"], lower=True, alpha=True)
    return [w for w in words if 4 <= len(w) <= 8 and len(set(w)) > 1]


def shuffle_letters(word):
    # Fisher-Yates shuffle, done by hand (random.shuffle is not allowed)
    letters = list(word)
    for i in range(len(letters) - 1, 0, -1):
        j = random.randint(0, i)                         # random position from 0 to i
        letters[i], letters[j] = letters[j], letters[i]  # swap the two letters
    return "".join(letters)


def scramble(word):
    # Shuffle again until the result is different from the original
    mixed = shuffle_letters(word)
    while mixed == word:
        mixed = shuffle_letters(word)
    return mixed


def play():
    word = random.choice(load_words())
    print(f"Unscramble this word: {scramble(word).upper()}")
    attempts = MAX_ATTEMPTS
    while attempts > 0:
        guess = input("$> ").strip().lower()
        if guess == word:
            print("Correct! Well done.")
            return
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")
    print(f"You lose! The word was {word.upper()}")


play()