#Finf the maximum value of tuplee
tup=(1,2,3,4,10,6,7,8)
print(max(tup))

#Minimumvalue of tuple
print(min(tup))

#convert tuple into list and modify then again turn that lisst into tuple
tup1=(1,2,3,4,5)
print("tuple:",tup1)#original tuple
list=list(tup1)#change tuple into list
print("list:",list)#list print
list.append(20)#add element into list
list[0]=0#change value at the inx 0
print("updated list:",list)#updated list print
tup2=tuple(list)#change that list into tuple
print("new updated tuple:",tup2)#new modified tuple

#Concatenate tuples
t=(1,2,3,4,5)
t2=(6,7,8,9,10)
tuple=t+t2#concatenated the both tup
print(tuple)#whole new tuple

#Slicing in tuple
print(tuple[6:])
print(tuple[-5:])#negative slicing(backword)

#Unpack tuple
t1=("ashi",21,"python")
name=t1[0]#storing the value throgh index
age=t1[1]
course=t1[2]
print("name:",name,"\nage:",age,"\ncourse:",course)