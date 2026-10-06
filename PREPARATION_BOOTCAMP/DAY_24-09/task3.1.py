ALPHABET = "abcdefghijklmnopqrstuvwxyz"

message = input("Enter the clear message: ")
key = int(input("Enter the key (1-25): "))

result = ""
for char in message:
    if char.lower() in ALPHABET:
        index = ALPHABET.index(char.lower())
        new_char = ALPHABET[(index + key) % 26]
        if char.isupper():
            new_char = new_char.upper()
        result += new_char
    else:
        result += char        # spaces, punctuation, numbers

print(result)