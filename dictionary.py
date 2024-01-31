a={'id':1,'name':'abc'}
print(a)
print(a['name'])
a['age']=18
print(a)
b={'course':'python'}
a.update(b)
print(a)
print(a.keys())
print(a.values())
print(a.items())
for i in a:
    print(a)