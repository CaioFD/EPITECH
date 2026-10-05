import random
from english_words import get_english_words_set

def words_of_length(words, n):
    return [w for w in words if len(w) == n]

def only_letters(words):
    return [w for w in words if w.isalpha()]

def group_by_length(words):
    groups = {}
    for w in words:
        n = len(w)
        if n not in groups:
            groups[n] = []           # first word of this length: create its list
        groups[n].append(w)
    return groups


# Part 1: test the 3 functions on words typed by the user
my_words = input("Type some words separated by spaces: ").lower().split()
n = int(input("Length to filter: "))
print("Words of length", n, ":", words_of_length(my_words, n))
print("Only letters:", only_letters(my_words))
print("Grouped by length:", group_by_length(my_words))

# Part 2: random word of the chosen length from the english-words package
words = only_letters(get_english_words_set(["web2"], lower=True))
n = int(input("\nLength of the random word: "))
candidates = words_of_length(words, n)
if candidates:
    print("Random word:", random.choice(candidates))
else:
    print(f"No word of length {n}.")