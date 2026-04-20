#Remove duplicate number from list.
l1=[1,2,3,1,2,3,4,5,6,7,5]
print("Original list before duplicate value removed: ",l1)
l2=[]#empty list
for num in l1:
    if num not in l2:#conditions
     l2.append(num) #Adding value in list
print("list after duplicate value remove: ",l2)#final list print

#Reverse the list(without slicing)
list=[1,2,3,4]
rev_list=[]#empty list
for i in range(len(list)-1,-1,-1):
   rev_list.append(list[i])
print(rev_list)

#Second largest number
l=[10,20,30,40]
max1=l[0]
max2=l[0]
for num in l: #conditions to check number
 if num>max1:
   max2=max1
   max1=num
 elif num>max2 and num!=max1:
   max2=num
print("Second largest number in list is" , max2)#print the second largest number

#Merge two list
list1=[1,2,3,4]
list2=[5,6,7,8,9]
result=list1+list2# using arthematic operator foe concatinating(Adding) the two list
print("Merge list: ",result)#print the full list after add