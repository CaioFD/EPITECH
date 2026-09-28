names = ["Joe", "William", "Jack", "Averell"]

print(sorted(names, key=len))                # shortest to longest
print(sorted(names, key=len, reverse=True))  #  longest to shortest