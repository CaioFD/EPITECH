from collections import Counter


def letter_frequency():
    try:
        with open("zen.txt") as file:
            letters = [c for c in file.read().lower() if c.isalpha()]
    except OSError as error:
        print(f"Error: {error}")
        return
    for letter, count in Counter(letters).most_common():
        print(f"{letter}: {count}")


letter_frequency()