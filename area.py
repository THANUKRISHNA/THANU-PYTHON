def square(a):
    return a*a
def rectangle(a,b):
    return a*b
def triangle(a,b):
    return 0.5*a*b
def calculator(a,b):
    c=input("enter the operation to perform,choose 1 to add,2 to minus,3 to multiply,4 to divide ")
    if c == '1':
        return a+b
    elif c == '2':
        return a-b
    elif c == '3':
        return a*b
    elif c == '4':
        return a/b
    