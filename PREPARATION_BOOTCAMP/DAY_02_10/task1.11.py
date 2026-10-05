def my_count(stop, start=0, step=1):
    if not all(type(n) is int for n in (stop, start, step)):
        print("Error: stop, start and step must be integers")
        return
    if step == 0:
        print("Error: step cannot be 0")
        return
    if (stop - start) * step < 0:   # passo na direção errada: inverte
        step = -step
    for n in range(start, stop, step):
        print(n)


my_count(100, -100, 42)
print("==================")
my_count(-100, 100, -42)
print("==================")
my_count(0, 3)
print("==================")
my_count(10, 0, 0)
print("==================")
my_count("toto")