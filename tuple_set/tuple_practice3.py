#sum of numbers in tuple
tup=(1,2,3,4,5)
result=sum(tup)
print(result)

#find even no. in tuple
even_no=()
for num in tup:
    if num%2==0:
     even_no=even_no+(num,)
print("even no:",even_no)
