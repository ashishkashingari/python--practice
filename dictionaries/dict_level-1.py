#create a dictionary
student = { #dict name
    "name":"Ashi",#keys of dict
    "age" : 20,
    "city":"Noida"
}

#Pint the values(name and age)
print(student["name"])#print the exisiting dict value-name
print(student["age"])#age

#Adding new value in exiting dict
student["course"]="Python"#added course in dict
print(student)#print whole dict 

#Update the value in dict
student["age"]=21#update
print(student["age"])#print the updated age
print(student)

#Remove the key from dict
del student["city"]
print(student)