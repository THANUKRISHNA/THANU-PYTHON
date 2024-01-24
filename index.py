#fahrenheit to celsius:
f=int(input("enter the fahrenheit:"))
c=(f-32)*5/9
print("fahrenheit to celsius:",c)
#kilometer to miles:
k=int(input("enter kilometer:"))
m=k*0.621371
print("kilometer to miles:",m)
if(c>100):
    print("printed:",c)
else:
    print("printed:",m)
#positive or negative:
a=int(input("enter the no: "))
if(a>=0):
    print("positive no:",a)
else:
    print("negative no:",a)
#or
if(a>0 or a<1):
    print("not zero:",a)
else:
    print("zero:",a)
#compare 3 no:
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
if(a>b and a>c):
    print("a is greater ")
elif(b>a and b>c):
    print("b is greater ")
else:
    print("c is greater ")
#3 table
a=3
b=1
while(b<=10):
    print(a,"*",b,"=",a*b)
    b=b+1
a="python"
for i in a:
    print(i)
a=3
for i in range(1,11,1):
    print(a,"*",i,"=",a*i)
for i in range(1,6,1):
    for j in range (1,i+1,1):
        print ("*",end=" ")
    print()
for i in range(1,6,1):
    for j in range(1,i+j,1):
        print(i)
for i in range(1,6,1):
    for j in range(1,i+i,1):
        print(i)
    print()
for i in range(1,6,1):
    for j in range(1,6,1):
         print(i*j,end=" ")
    print()
for i in range(1,6,1):
    a=input("enter password")
    if(a=="123"):
        print("correct")
        break
    else:
        print("wrong")
print("time over")