def new_division(num, den, acc=1):
    try:
        print(f"{num / den:.{acc}f}")
    except ZeroDivisionError:
        print("Error: division by zero")
    except (TypeError, ValueError):
        print("Error: num and den must be numbers, acc a positive integer")


new_division(8.4, 13)
new_division(8.4, 13, 10)
new_division(1, 0)