#Sum of list
l1=[1,2,3,4]
total=0
for i in l1:
 total +=i
print(total)

#Find maximum value in list
maximum=max(l1)
print("maximum value in list is: ",maximum)

#finding the minimum value from list
minimum=min(l1)
print("minimum value in list is: ",minimum)

#Count even and odd number in list
l2=[1,2,3,4,5,6,7,8]
even=[]
odd=[]
for num in l2:
    if num%2==0:
      even.append(num)
    else:
     odd.append(num)
print("Even numbers: ",even)
print("Odd numbers: ",odd)

#Search element in list
l3=[2,3,4,5,6,7,8,9]
num=int(input(("Enter the number which you want to find ")))
if num in l3:
     print("found")
else:
  ("Not found")
