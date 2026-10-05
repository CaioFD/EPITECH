def rewrite():
    try:
        with open("zen.txt") as source:
            content = source.read()
        with open("toto.txt", "w") as target:
            target.write(content)
    except OSError as error:
        print(f"Error: {error}")


rewrite()