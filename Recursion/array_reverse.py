x = [1,2,3,4,5]



def array_reverse(x,i):
    if len(x)//2 == i:
        return x
    x[i] , x[len(x)-i-1] = x[len(x)-i-1] , x[i]

    return array_reverse(x,i+1)

y = [1,2,3,4,5]

print(array_reverse(x,0))
print(array_reverse(y,0))