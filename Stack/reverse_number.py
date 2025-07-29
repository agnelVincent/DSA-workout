from Stack import Stack

def reverse_number(n):

    s = str(n)
    number = ''
    stack = Stack()

    for i in s:
        stack.push(i)

    while not stack.is_empty():
        number += stack.pop()

    return int(number)

print(reverse_number(12345))
