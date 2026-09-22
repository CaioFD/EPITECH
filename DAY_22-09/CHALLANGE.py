def gcd(a, b): #gratest common divisor
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): #lowest common multiple
    return a * b // gcd(a, b)

def lcm_range(n): 
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

print("LCM of numbers:") #lowest common multiple
print("Range of 1 to 20:")
print(lcm_range(20))
print("Range of 1 to 200:")
print(lcm_range(200))
print("Range of 1 to 2000:")
print(lcm_range(2000))


def gcd (a,b): 
    while b:
      a,b = b, a % b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

def lcm_range(b):
    result = 1 
    for i in range(1,b+1):
        result = lcm(result,i)
    return result