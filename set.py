'''a={'abc','bgy','pou'}
print(a)
a.add('vyt')
print(a)
a.remove('vyt')
print(a)
a.pop()
print(a)
b={'red','blue','green'}
c={'red','orange','black'}
d=b&c
print(d)
d=b-c
print(d)
d=b^c
print(d)
print(max(a))'''
b={'red','blue','green'}
c={'red','orange','black'}
for i in b:
    if b not in c:
        print('ok')
    else:
        print('no')