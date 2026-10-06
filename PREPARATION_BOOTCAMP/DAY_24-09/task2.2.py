text = input("Enter a string: ")

result = ""
for char in text:
    result += char * 2   # "t" * 2 == "tt"

print(result)