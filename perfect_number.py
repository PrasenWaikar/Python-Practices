n=496
temp=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if temp==sum:
    print("per")
else:
    print("not")