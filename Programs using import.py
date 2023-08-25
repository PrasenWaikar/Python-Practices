#heads or tails
'''import random

coin = random.randint(0,1)
if coin == 1 :
  print("Head")
else :
  print("tails")'''

#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
length=len(names)
a = random.randint(0 , length-1)
b=names[a]
print(b ,"will pay the bill")

# from math import sqrt as square,pi as p
# c=square(81)
# d=p*4
# print(c)
# print(d)
# import math as m
# print(dir(math))--------------------------->very important
# print(type(m.isqrt))