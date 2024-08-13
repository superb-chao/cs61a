from dis import dis
## Exception
def double(x):
    if x is not type(int):
        raise TypeError('需要int类型输入')
    return x+x

def invert(x):
    return 1/x

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print(e)


## Programming language