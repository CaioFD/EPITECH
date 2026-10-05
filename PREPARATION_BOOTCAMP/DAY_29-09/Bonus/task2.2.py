def frequency(word):
    counts = {}
    for c in word:
        counts[c] = counts.get(c, 0) + 1    # 0 the first time we see the letter
    return counts

def most_frequent(word):
    counts = frequency(word)
    best = None
    for letter in sorted(counts):           # alphabetical order -> wins the ties
        if best is None or counts[letter] > counts[best]:
            best = letter
    return best

word = input("Type a word: ").lower()
print(frequency(word))
print("Most frequent:", most_frequent(word))