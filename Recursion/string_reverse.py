x = 'Antonio Montana'

def str_reverse(s):
    if len(s) == 0:
        return ''
    return str_reverse(s[1:]) + s[0]

print(str_reverse(x))