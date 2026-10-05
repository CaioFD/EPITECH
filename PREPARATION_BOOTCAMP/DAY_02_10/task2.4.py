def count_lines(filename):
    try:
        with open(filename) as file:
            print(sum(1 for _ in file))
    except OSError as error:
        print(f"Error: {error}")


count_lines("zen.txt")
count_lines("primes.txt")