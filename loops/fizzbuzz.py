#print number 1 to 50.
#if number is divide by 3 and 5 print "FizzBuzz"
#if divide by 3 print "Fizz".
#if divided by 5 print "Buzz" otherwise print itself.
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
     print("Fizz")
    elif i%5==0:
       print("Buzz")
    else:
       print(i)    