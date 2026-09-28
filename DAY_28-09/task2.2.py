def clean(s):
    return "".join(c.lower() for c in s if c.isalnum())

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = input("Enter a string: ")
print(is_palindrome(clean(text)))