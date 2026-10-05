def my_division(a, b):
    try:
        quotient, remainder = divmod(a, b)
    except ZeroDivisionError:
        print("Error: division by zero")
        return None
    except TypeError:
        print("Error: both parameters must be integers")
        return None
    print("Quotiente: ", quotient, "Remainder: ", remainder)
    return quotient, remainder


my_division(42, 4)
my_division(42, 0)
my_division(42, 2)
my_division(42, 11)
my_division(42, "toto")