def contar_ocorrencias(text):
    text = text.lower()
    words = ["cat", "garden", "mice"]
    total = 0
    for Word in words:
        total += text.count(Word)
        total += text.count(Word[::-1])
    return total

text = input("Type a text: ")
print(contar_ocorrencias(text))