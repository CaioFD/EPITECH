VOWELS = "aeiou"

while True:
    number_text, _, text = input("Enter an integer and a string: ").partition(" ")
    number = int(number_text)

    if number == 0:
        break                                 

    has_vowel = any(char in VOWELS for char in text.lower())

    if has_vowel or number >= 42:
        print(number)
    else:
        print(text)