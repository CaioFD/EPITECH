print("Calculating the 6 first decimals of PI (continued fraction):")

n_terms = 100                  # essa fração continua converge bem mais rápido
resultado = 0
for i in range(n_terms, 0, -1):
    numerador = (2 * i - 1) ** 2      # 1, 3², 5², 7², ...
    resultado = numerador / (6 + resultado)

pi = 3 + resultado
print(f"PI: {pi:.6f}")