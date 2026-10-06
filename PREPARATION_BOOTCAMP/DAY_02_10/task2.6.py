def write():
    try:
        with open("toto.txt", "a") as file:
            file.write("I'm a new line\n")
    except OSError as error:
        print(f"Error: {error}")


write()