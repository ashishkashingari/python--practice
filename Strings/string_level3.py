#palindrome check
a="madam"
if a==a[::-1]:
     print("It is a Palindrome")
else:
     print("Not an palindrome")    

#Count the vowels
a=input("Enter the String: ")
vowels="a","e","i","o","u"
count=0
for v in vowels:
     count+=a.lower().count(v)
print(count)

#Remove spaces
b="hello world"
print(b.replace(" ",""))

#Replace the character
print(b.replace("world","everyone"))

#Count each Character
c="hello"
for ch in range(len(c)):
    print(c[ch],"=",ch)