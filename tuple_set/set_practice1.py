#set created and print
set={1,1,2,3,4}
print(type(set))#to know the type set or not
print(set)

#add elemnt to set
set.add(8)
print(set)

#remove element from set
set.remove(1)
print(set)

#remove raandom number
set.pop()
print(set)

#check element exist or not
num=8#finding the 8 in set or not
if num in set:#condition
    print("yes")
else:
    print("no")

#length of set
print(len(set))

#loop through set and print values
for num in set:
    print(num)

