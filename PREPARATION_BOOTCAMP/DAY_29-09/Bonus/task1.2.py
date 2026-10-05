def is_palindrome(word):
    word = word.lower()
    left = 0
    right = len(word) - 1
    while left < right:              # compare the two ends, moving to the middle
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


word = input("Type a word: ")
print(is_palindrome(word))