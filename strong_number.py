n=40585
temp=n
sum=0
while n>0:
    fact=1
    rem=n%10
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact 
    n=n//10
if temp==sum:
    print("strong")
else:
    print("not")