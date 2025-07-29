from Stack import Stack

def reverse_string(s):

    stack = Stack()
    reversed_string = ''

    for i in s:
        stack.push(i)
    if stack.is_empty():
        print('string is empty')
        return
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

print(reverse_string('Agnel'))
    