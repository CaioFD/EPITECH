def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:]) + text[0]

text = input("Type a text: ")
print(reverse_string(text))

