ALPHABET = "abcdefghijklmnopqrstuvwxyz"

ENGLISH_FREQ = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
                6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]

message = input("Enter the encrypted text: ")
key_length = int(input("Enter the key length: "))

letters = [c for c in message.lower() if c in ALPHABET]

key = ""                                         
for column in range(key_length):                 
    group = letters[column::key_length]          # every n-th letter, starting at "column"
    best_shift = 0                               
    best_score = 0                               
    for shift in range(26):                      # try all 26 possible shifts
        score = 0                                
        for c in group:                          # for each letter of the group
            decrypted_index = (ALPHABET.index(c) - shift) % 26  
            score += ENGLISH_FREQ[decrypted_index]               #add how common that letter is in English
        if score > best_score:                   
            best_score = score                   #  remember its score
            best_shift = shift                   # and remember the shift itself
    key += ALPHABET[best_shift]                  # turn the winning shift into a letter (10 -> "k")

print("Key found:", key)                         

result = ""
key_index = 0
for char in message:
    if char.lower() in ALPHABET:
        shift = ALPHABET.index(key[key_index % len(key)])
        new_char = ALPHABET[(ALPHABET.index(char.lower()) - shift) % 26]
        if char.isupper():
            new_char = new_char.upper()
        result += new_char
        key_index += 1
    else:
        result += char

print("Decrypted text:", result)

#test:
#Ikmkc ivss xksiyebuxv musla mlca xtammpn mh rnwv hw xuistaecb tw yymiqgk voi rwwi kawtty. Ajlr nwn xgzx nwnv rysvztq ypxw utra kmunxvgux xviyvz, cdc ympk xwm fmuaezml icypn igh avy hioi c ssi wy xkti aimit pr ipx ttvntkm.
#Decrypted text: Every good programmer knows that testing is just as important as writing the code itself. When you test your program with many different inputs, you find the mistakes early and you save a lot of time later in the project.
#Key found: epitech