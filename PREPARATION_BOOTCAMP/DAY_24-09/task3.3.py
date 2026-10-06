ALPHABET = "abcdefghijklmnopqrstuvwxyz"

mode = input("Type 'e' to encrypt or 'd' to decrypt: ")
message = input("Enter the message: ")
key = input("Enter the key (letters only): ").lower()

result = ""
key_index = 0                    
for char in message:
    if char.lower() in ALPHABET:
        shift = ALPHABET.index(key[key_index % len(key)])
        if mode == "d":
            shift = -shift         
        index = ALPHABET.index(char.lower())
        new_char = ALPHABET[(index + shift) % 26]
        if char.isupper():
            new_char = new_char.upper()
        result += new_char
        key_index += 1             # next letter of the key
    else:
        result += char           

print(result)