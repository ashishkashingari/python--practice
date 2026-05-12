#acces the element of tuple
tup=(10,20,30,40)#tuple created
print(type(tup))#for know its tuple or not
print(tup[:3])#element access at the index 3
print(tup[-2:])# from backward access 2 index(2 last)
print(tup[2])#access 2 element of  tuple

#length of tuple
print(len(tup))

#loop through the tuple
for i in tup:
    print(i)

#count the occurences
count=tup.count(10)
print(count)

#check the particular num exists in tuple of not(ex-30)
num=30
if num in tup:
    print("yes\nnumber finded at the index:",tup.index(num))
else:
    print("no")

#Single element tup
tuple=(1,)
print(type(tuple))
print(tuple)