#print only odd numbers from 1 to 10 using loops.
#for loop
for i in range(1,11):#using 11 because last number is not executed in loop.
      if i%2==0:
          continue
      print(i)
    
    #using while loop
a=1
while a<10:
     if a%2==0:
         a+=1
         continue
     print(a)  
     a+=1  