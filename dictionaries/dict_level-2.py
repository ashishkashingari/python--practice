#Loop through dictionary
student = { #dict name
    "name":"Ashi", #keys of dict
    "age" : 20,
}
for key in student: #loop start
    student[key]
print(student[key])#print studentkeys

#Count frequency (input hello)
dict_freq={}#empty dict
s=input("Enter the string: ")#taking input from user
for char in s:#loop
 if char in dict_freq:#condition
    dict_freq[char]+=1
 else:
    dict_freq[char]=1
for key in dict_freq:#for print the frequency
 print(key, ":" ,dict_freq[key])