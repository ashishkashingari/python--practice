#even and odd using return function
def even_odd(n):#create function
    if n%2==0:#conditions
        return("Even")
    else:
        return("Odd")
print(even_odd(2))#store and print the result
print(even_odd(7))    
#method 2

def odd_even(n):#function create
    if n%2==0:#conditions
        return("Even")
    else:
        return("Odd")
result= odd_even(9)#output=odd store value in result
print(result) #print that store value result
result= odd_even(4)#output=even
print(result) 
