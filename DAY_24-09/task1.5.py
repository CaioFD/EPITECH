number = int(input("Type a number: "))
result = ""
if number == 42:               result += "a "
if number <= 21:               result += "b "
if number % 2 == 0:            result += "c "
if number / 2 < 21:            result += "d "
if number % 2 != 0 and number >= 45: result += "e "
if result == "":               result = "f"
print(result)