def is_anagram(word1, word2):
    # Same letters, same number of times -> same list once sorted
    return sorted(word1.lower()) == sorted(word2.lower())


word1 = input("First word: ")
word2 = input("Second word: ")
print(is_anagram(word1, word2))