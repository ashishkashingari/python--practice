#acces the element of tuple
tup=(10,20,30,40)
print(type(tup))
print(tup[:3])
print(tup[-2:])
print(tup[2])

#length of tuple
print(len(tup))

#loop through the tuple
for i in tup:
    print(i)

#count the occurences
count=tup.count(10)
print(count)
