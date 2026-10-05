def my_sum(*args):
    try:
        print(sum(args))
    except TypeError:
        print("ValueError: all arguments must be numbers")


my_sum(1)
my_sum(1, 2, 3)
my_sum(-20, -10, 5, 5, 10, 10)
my_sum(1, "toto")