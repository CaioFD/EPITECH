def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")

def sandwich(veg=False):
    bread()
    if veg:
        lettuce()
        lettuce()
        tomato()
        tomato()
    else:
        lettuce()
        tomato()
        ham()
        ham()
    bread()

def make_sandwiches(n, veg=False):
    for _ in range(n):
        sandwich(veg)
        print()

text = input("How many sandwiches? ")
answer = input("Vegetarian? (y/n): ")

veg = answer.strip().lower() == "y"

if text.isdigit():
    make_sandwiches(int(text), veg)
else:
    print("I can't do this!")