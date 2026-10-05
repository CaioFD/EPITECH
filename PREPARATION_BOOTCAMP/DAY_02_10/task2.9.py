import re
from collections import Counter


def word_frequency():
    try:
        with open("zen.txt") as file:
            words = re.findall(r"[a-z']+", file.read().lower())
    except OSError as error:
        print(f"Error: {error}")
        return
    for word, count in Counter(words).most_common():
        print(f"{word}: {count}")


word_frequency()