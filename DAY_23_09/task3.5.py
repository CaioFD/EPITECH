text = input("Enter a text: ")

def letter_frequency(text): 
    text = text.lower()
    frequency = {}
    for letter in text:
        if letter.isalpha():
            frequency[letter] = frequency.get(letter, 0) + 1

    total = sum(frequency.values())
    return {letter: count / total * 100 for letter, count in frequency.items()}

LANGUAGES = {
    "portuguese": {"e": 12, "a": 13.5, "i": 6.2, "n": 5.0, "o": 10.7, "r": 6.5, "s": 7.8, "t": 4.3,
                   "l": 5, "d": 5.0, "u": 5, "m": 4.7, "c": 3.9, "p": 2.5},

    "dutch": {"e": 15, "a": 9.5, "i": 6.5, "n": 8, "o": 6.1, "r": 6.4, "s": 3.7, "t": 6.8,
              "l": 3.6, "d": 5.9, "u": 2.0, "m": 2.2, "c": 1.2, "p": 1.6},

    "german": {"e": 10, "a": 8.9, "i": 8.2, "n": 10, "o": 7.6, "r": 4.7, "s": 4.3, "t": 3.9,
               "l": 4, "d": 3.3, "u": 2.5, "m": 2.8, "c": 3.9, "p": 3.1},
}

def guess_language(text_frequency):
    best_language = None
    smallest_difference = None

    for language, reference_frequency in LANGUAGES.items():
        difference = sum(
            (text_frequency.get(letter, 0) - percentage) ** 2
            for letter, percentage in reference_frequency.items()
        )
        if smallest_difference is None or difference < smallest_difference:
            smallest_difference = difference
            best_language = language
    return best_language


frequency = letter_frequency(text)
for letter, percentage in sorted(frequency.items(), key=lambda x: -x[1]):
    print(f"{letter} = {percentage:.1f}%")
print(f"Probable language: {guess_language(frequency)}")