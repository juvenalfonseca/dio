

def soma(*args):
    t = 0
    for n in args:
        t += n
    return t

def subtrai(*args):
    t = 0
    for n in args:
        t -= n
    return t

def multiplica(*args):
    t = 0
    for n in args:
        t *= n
    return t

def divide(num1, num2):
    try:
        t = num1 / num2
    except:
        t = 0
    return t

