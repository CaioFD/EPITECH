number = input("Type a number: ")
try:
    value = int(number)
except ValueError:
    try:
        value = float(number)
    except ValueError:
        value = number

print(type(value))