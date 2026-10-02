def check_even(number):
    return number % 2 == 0


print(list(filter(check_even, [1, 2, 3, 4, 5, 6])))