import random
import time

start = time.time()

numbers = [random.randint(0, 1000000) for _ in range(1000000)]
print(f"List created in {time.time() - start:.2f} s")

sort_start = time.time()
numbers.sort()          # Python's built-in sort (Timsort, written in C)
print(f"List sorted in {time.time() - sort_start:.2f} s")

print("First 10:", numbers[:10])
print("Last 10:", numbers[-10:])
print(f"Total time: {time.time() - start:.2f} s")

# List created in 0.47 s
# List sorted in 0.36 s
# First 10: [1, 1, 2, 3, 3, 3, 3, 5, 6, 6]
# Last 10: [999992, 999992, 999995, 999996, 999997, 999998, 999998, 999998, 999998, 999999]
# Total time: 0.83 s