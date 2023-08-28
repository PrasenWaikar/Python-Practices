num=int(input("enter value : "))
rev=0
temp=num
while temp > 0:
    a=temp%10
    rev=rev*10+a
    temp=temp//10

print(rev)
if rev == num:
    print("palindrome")
else:
    print("not palindrome")