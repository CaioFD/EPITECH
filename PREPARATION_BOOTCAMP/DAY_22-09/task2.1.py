# generates the terms 1, 11, 111, ..., 111111111 
terms = [int('1' * n) for n in range(1, 10)]
total = sum(terms)

print("Sum 1:")
print("1 + 11 + 111 + ... + 111111111 =", total)

print("Powers of the sum:")
print("  total ** 2 =", total ** 2)
print("  total ** 3 =", total ** 3)
print("  total ** 4 =", total ** 4)
print("  total ** 5 =", total ** 5)

