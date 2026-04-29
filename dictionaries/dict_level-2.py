# #Loop through dictionary
student = { #dict name
     "name":"Ashi", #keys of dict
     "age" : 20,
 }
for key in student: #loop start
     student[key]
print(student[key])#print studentkeys

#Count frequency 
dict_freq={}#empty dict
s=input("Enter the string: ")#taking input from user
for char in s:#loop
  if char in dict_freq:#condition
     dict_freq[char]+=1
  else:
     dict_freq[char]=1
for key in dict_freq:#for print the frequency
  print(key, ":" ,dict_freq[key])

 #Sum of values
marks={ #dict
   "English":90,
   "Maths":80,
   "Science":85,
 }
total=0#variable to store sum of values
for num in marks.values():#loop  which go thorugh all key value
 total+=num #add values
print("Sum of all values are:",total)#print the sum of key values

#Find max  value in dict
max_val=0
for key in marks:#loop 
 marks[key]
 if marks[key]>max_val:
  max_val=marks[key]
print("max value is:",max_val)

#Search key in dict
key=input("Enter key: ")
if key in student:
 print("Found")
else:
  print("Not found")
