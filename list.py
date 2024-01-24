a=[1,2,3,4,5]
for i in a:
    print(i)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
a.append(6)
print(a)
b=[10,20]
a.extend(b)
print(a)
a.insert(2,9)
print(a)
a.insert(2,b)
print(a[2])
print(a[2][0])
a.remove(2)
a.pop()
a.clear()
del a
s=0
a=[1,2,3,4,5]
for i in range(0,len(a)):
    s=s+a[i]
print(s)

    