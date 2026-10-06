def count_types(text):
    vowels = 0
    consonants = 0
    for c in text.lower():
        if not c.isalpha():          # skip spaces, digits, punctuation
            continue
        if c in "aeiou":
            vowels += 1
        else:
            consonants += 1
    print(f"{vowels} vowels, {consonants} consonants")


text = input("Type a text: ")
count_types(text)