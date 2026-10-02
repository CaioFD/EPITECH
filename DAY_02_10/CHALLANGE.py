import sys

UNITS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]


def words(n):
    if n < 20:
        return UNITS[n]
    if n < 100:
        return TENS[n // 10] + UNITS[n % 10]
    if n < 1000:
        rest = "and" + words(n % 100) if n % 100 else ""
        return UNITS[n // 100] + "hundred" + rest
    rest = n % 1000
    link = "and" if 0 < rest < 100 else ""
    return words(n // 1000) + "thousand" + link + words(rest)


def count_letters(n):
    return sum(len(words(i)) for i in range(1, n + 1))


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        if not 1 <= n <= 999999:
            raise ValueError
    except (IndexError, ValueError):
        sys.exit("Usage: python challenge.py N   (N integer from 1 to 999999)")
    print(count_letters(n))