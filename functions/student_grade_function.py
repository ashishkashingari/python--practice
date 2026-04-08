#calculate the grade of student marks with the use of percentage.
def grade(m1,m2,m3,m4,m5):#create function for grade
    total=m1+m2+m3+m4+m5#Total the marks for percentage.
    p=total/5# percentage
    if p>=90:#condition for grade check
        print("A+")
    elif p>=70:
        print("A")
    elif p>=60:
        print("B+")
    elif p>=50:
        print("B")
    elif p>=35:
        print("C")
    else:
        print("Fail")
grade(10,50,80,30,50)#calling the function
grade(10,5,10,2,4)