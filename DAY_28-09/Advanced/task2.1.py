def find_longest_word(words):
    return max(words, key=len)

n = int(input("How many words? "))

words = []
for i in range(n):
    word = input(f"Word {i + 1}: ")
    words.append(word)

print("Longest word:", find_longest_word(words))