import time  

def power(base, exp):
    result = 1                 
    while exp > 0:              
        if exp % 2 == 1:        # if the exponent is odd...
            result *= base      # keep one copy of the base in the result

        base *= base            # square the base: b, b^2, b^4, b^8...
        exp //= 2               # cut the exponent in half (integer division)

    return result               # the final answer


user_base = int(input("Enter the base: "))
user_exp = int(input("Enter the exponent: "))

for b, e in [(user_base, user_exp), (42, 84), (42, 168)]:
    t = time.perf_counter()    
    r = power(b, e)             
    print(f"{b}^{e} = {r}")    
    # stop the stopwatch: elapsed seconds * 1,000,000 = microseconds (µs)
    # :.1f it's to show only 1 decimal place 
    print(f"time: {(time.perf_counter() - t) * 1e6:.1f} µs\n")