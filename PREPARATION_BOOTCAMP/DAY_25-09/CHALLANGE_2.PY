LETTER_SCORES = {
    "AEIOULNSTR": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
}

def scrabble_score(word):
    score = 0
    for letter in word.upper():                      
        for letters, points in LETTER_SCORES.items(): # find the group of the letter
            if letter in letters:
                score += points
    return score

word = input("Enter a word: ")
print(f"The word {word} is worth {scrabble_score(word)} points")

print("===========================")

print(scrabble_score("cabbage"))   # 14
print(scrabble_score("Python"))    # 14
print(scrabble_score("quiz"))      # 22