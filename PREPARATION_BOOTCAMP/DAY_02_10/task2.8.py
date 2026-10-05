import re


def longest():
    try:
        with open("zen.txt") as file:
            words = re.findall(r"[a-z']+", file.read().lower())
    except OSError as error:
        print(f"Error: {error}")
        return
    if not words:
        print("Error: zen.txt has no words")
        return
    print(max(words, key=len))


longest()