def read_lines(*numbers):
    try:
        with open("primes.txt") as file:
            lines = file.read().splitlines()
    except OSError as error:
        print(f"Error: {error}")
        return
    for number in numbers:
        if type(number) is not int or not 1 <= number <= len(lines):
            raise ValueError(f"primes.txt has no line {number}")
        print(lines[number - 1])


read_lines(666)
read_lines(1, 2, 3)
#read_lines(20000)