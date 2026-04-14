# #Create a list
l=[]#Empty list
print(type(l))#type casting to know the data type.
l.append(1)#for single num add in list at the end of list
print(l)

# #input 5 numbers in list from user.
l1=[]
for i in range(6):
 num=int(input("Enter the five values:  "))
 l1.append(num)
print(l1)

#print entire list then print only first and last element
l2=[1,2,3,4,5,6]
print("Entire list is: ",l2)
print("The first element of list is: ",l2[:1])
print("The last element of list is: ",l2[-1:])

#insert number in list at a particular position
l2.insert(3,0)
print(l2)

#Remove perticular element from list
l2.remove(1)
print(l2)