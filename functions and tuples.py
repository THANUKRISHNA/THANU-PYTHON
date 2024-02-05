a=(1,2,3)
print(a[0])
print(a*2)
print(a[0:2])
b=(4,5,6)
print(a+b)
d=list(a)
print(d)
a=tuple(d)
print(a)

#functions:
def cube():
    a=int(input("enter the number"))
    print(a**3)
cube()


def cube1():
    a=int(input("enter the number"))
    return a**3
print("cube value is",cube1())

def add(a,b):
    print(a+b)
add(90,85)

def my(name,age):
    print(name," ",age)
my("abc",10)
my(age=21,name="jhg")
