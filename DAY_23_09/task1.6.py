text = "tutu on the tuki-kata"
result = ""
pular = 0

for i in range(len(text)):
    if pular > 0:
        pular -= 1
        continue
    if text[i:i+2] == "tu":
        result += "ta"
        pular = 1
    else:
        result += text[i]

print(result)
