from collections import deque

print("1 - add new item")
print("2 - remove item from list")
print("3 - show list")
print("4 - quit")

stack = deque()


def push():
    n = input("what you want to add?: ")
    stack.appendleft(n)


def pop():
    n = input("what you want to remove?: ")
    if n in stack:
        stack.remove(n)

    if n not in stack:
        print("There are not such element")


def show_list():
    print(stack)


m = 0
while m != 4:
    m = int(input("what you want to do? "))
    if m == 1:
        push()

    if m == 2:
        pop()

    if m == 3:
        show_list()
