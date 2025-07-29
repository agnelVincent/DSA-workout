x = [1,2,[3,4],5,[6,7,8],[9,10,11,12],13,[14]]

def flatten_array(x):
    y = []
    for i in x:
        if isinstance(i,list):
            y += flatten_array(i)
        else:
            y.append(i)

    return y

print(flatten_array(x))