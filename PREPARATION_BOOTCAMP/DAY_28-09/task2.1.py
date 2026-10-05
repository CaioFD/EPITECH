def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n - 1)

n = int(input("Type a number: "))
print(sum_to(n)) 