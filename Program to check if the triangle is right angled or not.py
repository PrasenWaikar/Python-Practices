a=int(input("enter the first side : "))
b=int(input("enter the second side : "))
c=int(input("enter the third side : "))
first_side=pow(a,2)
second_side=pow(b,2)
third_side=pow(c,2)
if first_side==second_side + third_side:
    print("Right angle triangle")
else:
    print("Not a right angle triangle")