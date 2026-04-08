#sum of even numbers 1 to 20.
#for loop
sum=0
for i in range(1,21):
    if i%2==0:
        sum=sum+i
print(sum)

#while loop
sum=0
a=1
while a<=20:
   if a%2==0:
    sum=a+sum
   a+=1
print(sum)
   