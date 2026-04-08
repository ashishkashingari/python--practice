n=121
original =n
rev=0
while n>0:
  last=n%10
  rev=rev*10+last
  n=n//10
if rev==original:
     print("palindrome")
else:
       print("not an palindrome")