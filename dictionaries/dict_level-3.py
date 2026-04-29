#Invert a dictionary
dict1={"a":1,"b":2,"c":3}#main dict
dict2={}#empty dict later use for invert val
for key in dict1:#loop so all key and value access
    value=dict1[key]#swaping the keya and val
    dict2[value]=key
print(dict2)#print the inverted dict key val

#Merge two dictionaries
d1={"a":1,"b":2}
d2={"c":3,"d":4}
d1.update(d2)#directly update the dict1
print(d1)
#method-2
for key in d2:#using loop 
    d1[key]=d2[key]
print(d1)

#Key with max value
marks={"maths":70,"science":80,"english":75}#dict
max_val=0#minimum max value
max_key=""
for key in marks:#loop to go through the dict keys
    if marks[key]>max_val:#condition
        max_val=marks[key]#update the max value when condition is apply
        max_key=key#track key and update
print(max_key)#print the max value

#Remove the duplicate values
dicti1={"a":1,"b":2,"c":1}
seen=[]
dicti2={}
for key in dicti1:
    value=dicti1[key]
    if value not in seen:#condition
     seen.append(value)#add value
     dicti2[key]=value
    else:
        continue#if value  is duplicate skip it
print(dicti2)#print dicti without the duplicate val

#Word frequency
dict_word={}
s=input("Enter the words:")
words=s.split()#break string into word
freq={}
for word in words:#condition for check 
    if word in freq:
        freq[word]+=1#increase by 1
    else:
        freq[word]=1
for key in freq:
    print(key,":",freq[key])#print 