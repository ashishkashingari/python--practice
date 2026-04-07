def grade(m1,m2,m3,m4,m5):#create function for grade
    total=m1+m2+m3+m4+m5#Total the marks for percentage.
    p=total/5# percentage
    if p>=90:#condition for grade check
        return("A+")
    elif p>=70:
       return("A")
    elif p>=60:
        return("B+")
    elif p>=50:
        return("B")
    elif p>=35:
        return("C")
    else:
        return("Fail")
#method 1   first store result then print
result=grade(90,80,70,60,80)
print(result)
#method 2 direct print 
print(grade(10,50,80,30,50))
print(grade(10,5,10,2,4))

