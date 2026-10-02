def read_file():
    try:
        with open("primes.txt") as file:
            content = file.read()
    except OSError as error:
        print(f"Error: {error}")
        return
    print(content if content else "Error: primes.txt is empty")


read_file()