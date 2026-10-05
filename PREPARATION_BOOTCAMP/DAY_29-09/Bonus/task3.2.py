MAX_PENALTIES = 12
ROUNDS = 3


def ask_secret(name):
    while True:
        secret = input(f"{name}, type the secret word: ").strip().upper()
        if secret.isalpha() and len(secret) >= 3:
            print("\n" * 50)                 # "clear" the terminal to hide the word
            return secret
        print("Letters only, at least 3 letters.")


def play_round(word, name):
    found = set()
    wrong = set()
    penalties = 0
    print(f"{name}, your turn to guess!")
    while True:
        hidden = " ".join(c if c in found else "_" for c in word)
        print(f"{hidden} / {penalties} penalties")
        if wrong:
            print("Wrong letters:", ", ".join(sorted(wrong)))

        guess = input("$> ").strip().upper()
        if not guess.isalpha():
            print("Please type only letters.")
        elif len(guess) == 1:
            if guess in found or guess in wrong:
                print(f"'{guess}' was already tried")
            elif guess in word:
                found.add(guess)
            else:
                wrong.add(guess)
                penalties += 1
        elif guess == word:
            found = set(word)
        else:
            penalties += 5
            print(f"{guess}: incorrect guess")

        if set(word) <= found:
            print(f"{word}: found with {penalties} penalties!\n")
            return penalties
        if penalties >= MAX_PENALTIES:
            print(f"Lost! The word was {word}\n")
            return penalties


names = [input("Player 1 name: "), input("Player 2 name: ")]
scores = [0, 0]                            

for r in range(1, ROUNDS + 1):
    print(f"\n===== Round {r} =====")
    for chooser in (0, 1):
        guesser = 1 - chooser      # the other player (0 <-> 1)
        secret = ask_secret(names[chooser])
        scores[guesser] += play_round(secret, names[guesser])
    print(f"Score: {names[0]} {scores[0]} - {names[1]} {scores[1]} penalties")

print("\n===== Final result =====")
if scores[0] < scores[1]:
    print(f"{names[0]} wins with {scores[0]} penalties!")
elif scores[1] < scores[0]:
    print(f"{names[1]} wins with {scores[1]} penalties!")
else:
    print(f"It's a tie: {scores[0]} penalties each!")