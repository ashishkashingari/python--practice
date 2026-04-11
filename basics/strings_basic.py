a=input("Enter a string: ")
#To find the length of string
print(len(a))
#print from index(positive indexing)
print(a[0:])
#print from last (negative indexing)
print(a[-1:])#always start from -1
#Indexing from 1 index to 6th index( 6th index value is not excte only till 5th index)
print(a[1:6])
#Check the string ends with "ow".always return boolean value(True/False)
print(a.endswith("ow"))
#Check the starting with value of string
print(a.startswith("he"))
#Count the given variable in string
print(a.count("L"))
