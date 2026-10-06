def create_file():
    try:
        open("toto.txt", "w").close()
    except FileExistsError:
        print("toto.txt already exists")
    except OSError as error:
        print(f"Error: {error}")


create_file()