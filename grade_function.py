#programe to calculate grade based on a single number(marks).
def grade(n):#creating function
    if n>=90:#condition to check grade for number
        print("A+")
    elif n>=70:
        print("A")
    elif n>=60:
        print("B+")
    elif n>=50:
        print("B")
    elif n>=30:
        print("C")
    else:
        print("Fail")
grade(10)#calling function
grade(50)        
