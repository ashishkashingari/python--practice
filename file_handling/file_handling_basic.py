#create file and write
file=open("hello.txt","w")
file.write("hello eveyone. I'm learning the python")
file.close()

#read the  file
file=open("hello.txt","r")
content=file.read()
file.close()
print(content)

#Append the file
file=open("hello.txt","a")
file.write("\nnow  i am learning file handling concept")
file.close()