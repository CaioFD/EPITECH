print("Calculating the 6 first decimals of PI:")

pi = 0
n_terms = 900_000# o suficiente pra estabilizar as 6 primeiras casas
for i in range(n_terms):
    term = 1 / (2 * i + 1)
    pi += term if i % 2 == 0 else -term
pi *= 4
print(f"PI: {pi:.6f}")