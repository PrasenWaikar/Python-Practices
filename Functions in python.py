# functions
'''
def calculation(a,b):
  print("Addition : ",a+b)

def compare(a,b):
  if a > b :
    print(a,"is greater")
  else :
    print(b,"is greater")

def mean(a,b):
  pass

def the_end():
  print("End of all functions")

def average(a,b):
  print("The average is : ",int((a+b)/2))

average(2,4)


a=int(input("Enter value for a : "))
b=int(input("Enter value for b : "))

calculation(a,b)
compare(a,b)
the_end()
'''

# functions and arguments


# 1)--------Default argument
"""
def average(a,b=2):
  print("The average is : ",int((a+b)/2))

average(a=9)
"""

# 2)--------Keyword argument
'''
def average(a=8,b=4):
  print("The average is ",(a+b)/2)

average(a=4,b=2)
'''

# 3)--------Variable length argument
'''
def adder(x,y,z):#
  print(x+y+z)#---------------------------this will give error

adder(2,1,2,3)#
'''
# solution
'''
def adder(*num):               #--------(*args)
  sum = 0
  for n in num :
    sum = sum + n
  print(sum)

adder(52,9848,56181,123,45648,45)
'''

# 4)--------Required argument (In this we have to give all the values for variables)
'''
def average(a=8,b=4):
  print("The average is ",(a+b)/2)

average(a,b=2)
'''
'''
n=5
fact = 1
for i in range(1,n+1):
  fact = fact * i
print(fact)
'''

#Factorial program using functoin
'''
def fact(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  print(fact)

fact(4)
'''

#Factorial program using recursive function
#Recursion calling a function in a function
'''
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(7))
'''

#fibonacci series
'''
a = int(input("Enter any number : "))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(a):
    print(fibonacci(i))
'''
