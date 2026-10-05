def bread():
    print("<//////////>")
def lettuce():
    print("~~~~~~~~~~~~")
def tomato():
    print("O O O O O O")
def ham():
    print("============")

def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

def make_sandwiches(n):
    for _ in range(n):
        sandwich()
        print()
        print()

text = input("How many sandwiches? ")

if text.isdigit():
    make_sandwiches(int(text))
else:
    print("I can't do this!")