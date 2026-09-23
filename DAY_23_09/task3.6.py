def letter_frequency(text):
    text = text.lower()
    freq = {}
    for letter in text:
        if letter.isalpha():
            freq[letter] = freq.get(letter, 0) + 1
    total = sum(freq.values())
    return {letter: count / total * 100 for letter, count in freq.items()}

LANGUAGES = {
    "portuguese": {"e": 12, "a": 13.5, "i": 6.2, "n": 5.0, "o": 10.7, "r": 6.5, "s": 7.8, "t": 4.3,
                  "l": 5, "d": 5.0, "u": 5, "m": 4.7, "c": 3.9, "p": 2.5},
    "dutch": {"e": 15, "a": 9.5, "i": 6.5, "n": 10.0, "o": 6.1, "r": 6.4, "s": 3.7, "t": 6.8,
             "l": 3.6, "d": 5.9, "u": 2.0, "m": 2.2, "c": 1.2, "p": 1.6},
    "german":   {"e": 7.6, "a": 8.9, "i": 8.2, "n": 5.5, "o": 7.6, "r": 4.7, "s": 4.3, "t": 3.9,
                  "l": 2.1, "d": 3.3, "u": 2.5, "m": 2.8, "c": 3.9, "p": 3.1},
}

def guess_language(text_freq):
    best_language = None
    smallest_difference = None
    for language, reference_freq in LANGUAGES.items():
        difference = sum((text_freq.get(letter, 0) - pct) ** 2 for letter, pct in reference_freq.items())
        if smallest_difference is None or difference < smallest_difference:
            smallest_difference = difference
            best_language = language
    return best_language

path = input("Enter the file path: ")
with open(path, "r", encoding="utf-8") as file:
    text = file.read()

freq = letter_frequency(text)
for letter, pct in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"{letter} = {pct:.1f}%")

print(f"Probable language: {guess_language(freq)}")