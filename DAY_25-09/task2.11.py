numbers = {
    "dalmatians": 101,
    "pi": 3.14,
    "beast": 666,
    "life": 42,
    "googol": 10 ** 100,     
    "jordan": 23,
    "life, the universe and everything": 42,
    "emergency": 911,
    "euler": 2.71828,
}

best_key = None
for key in numbers:
    if best_key is None or numbers[key] > numbers[best_key]:
        best_key = key
print(best_key)
