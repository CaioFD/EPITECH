def read_line():
    try:
        with open("zen.txt") as file:
            for line in file:
                print(line, end="")
    except OSError as error:
        print(f"Error: {error}")


read_line()