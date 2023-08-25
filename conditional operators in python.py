# >   <   >=   <=   ==   !=
#If Else Conditional Statements
# age = int(input("enter your age : "))
# print("your age is : ", age)
# print(age > 18)
# print(age < 18)
# print(age >= 18)
# print(age >= 18)
# print(age != 18)
# print(age == 18)
'''
#if else
if (age > 18) :
  print("you can drive")
  print("yes")
else :
  print("you cannot drive")
  print("no")
print("yeh!!!!")
'''

#elif statement
'''
num = int(input("enter value for num : "))
if num < 0 :
  print("Number is negative")
elif num == 0 :
  print("Number is zero")
elif num == 999 :
  print("Number is Special")
else :
  print("number is positive")
  '''

#nested if else
'''
num = int(input("enter value for num between 10 - 50 : "))

if num < 0 :
  print("Number is less than 0")
elif num > 0:
  print("Number is greater than 0")
  if num > 10 and num < 20 :
    print("Number is between 10 - 20")
  elif num > 20 and num < 30 :
    print("Number is between 20 - 30")
  elif num > 30 and num < 40 :
    print("Number is between 30 - 40")
  else :
    print("But number is greater than 50 ")
else :
  print("Number is negative")

print("End of nested if else")
'''

'''water_level=80
if water_level > 80 :
  print("drain the water")
else :
  print("continue")'''
'''print("WELCOME TO ROLLERCOASTER")
height = int(input("enter the height in cm : "))
if height >= 120 :
  print("proceed")
else : 
  print("do not proceed")'''

# EVEN OR ODD
'''number = int(input("Enter number to check : "))
if number % 2 == 0 :
  print("number is even")
else : 
  print("number is odd")'''

# nested if else
'''height  = int(input("enter height in cm : "))
age = int(input("enter the age : "))

if height >= 120 :
  print("you can proceed")  
  if age <= 12 :
    print("pay 7 rs for tickets.")
  else:
    print("pay 12 rs for tickets.")
else:
  print("can't proceed for ride")'''

# Elif

'''height = int(input("enter height in cm : "))
if height >= 120 : 
  print("Proceed")
  age = int(input("enter your age : "))

  if age < 7 :
    print("pay 5 rs for tickets.")
  elif age <= 18 :
    print("pay 12 rs for tickets.")
  elif age > 18 :
    print("pay 17 rs for tickets.")

else :
    print("can't proceed")'''

#---------------------short hand ifelse
# a=100
# b=200
# print("A" if a > b else print("=") if a==b else print("B"))
# c = 9 if a < b else 0
# print(c)