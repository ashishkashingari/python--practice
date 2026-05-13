with open("file.txt","w")as file:
   file.write("Python\nJava\nC++")

 #read file and print line by line
with open("file.txt","r")as file:
 for line in file:
    print(line)
#count total lines in file
with open("file.txt","r")as file:
  count=0
  for line in file:
   count+=1
print(count) 

#check does file exit before opening it
import os
if os.path.exists("file.txt"):
 with open("file.txt","r")as file:
   print(file.read())
else:
  print("file not found")
  
