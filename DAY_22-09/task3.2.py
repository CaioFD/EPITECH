def sum_digits(n):
    return sum(int(d) for d in str(n))

print("Sum of the digits of 123456789:")
print(sum_digits(123456789))

print("Sum of the digits of 112233445566778899:")
print(sum_digits(112233445566778899))

print("Sum of the digits of 123456789 * 987654321:")
print(sum_digits(123456789) * sum_digits(987654321))

num = int(input("Enter a number: "))
print("Sum of the digits of", num, ":")
print(sum_digits(num))