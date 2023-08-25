num=int(input("enter a number : "))
check=0
for i in range(2,num):
    if num%i==0:
        check=1
        break

if check == 1:
    print("Not a prime")
else:
    print("It is a prime")


