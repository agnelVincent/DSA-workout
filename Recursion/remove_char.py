x = 'hello world'

def remove_char(s , char):
    if len(s) == 0:
        return ''
    if s[0] == char:
        return remove_char(s[1:],char)
    else:
        return s[0] + remove_char(s[1:],char)
    
print(remove_char(x,'l'))