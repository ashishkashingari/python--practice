#print number 1 to 5 but skip number 3.
#using for loop.

for i  in range(1,6):
     if i==3:
         continue
     print(i)
     i+=1


# using while loop
b=1
while b<=5:
    if b==3:
         b+=1
         continue
    print(b)
    b+=1

