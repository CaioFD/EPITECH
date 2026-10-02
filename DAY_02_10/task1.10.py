def my_count(stop, start=0):
    if type(stop) is not int or type(start) is not int:
        print("Error: stop and start must be integers")
        return
    for n in range(start, stop):
        print(n)


my_count(5)
print("=====================")
my_count(5, 2)