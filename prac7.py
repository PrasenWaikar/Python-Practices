# s='pqrstpprstpasw'
# a=set(s)
# print(len(a))

# sample = "This is a sample test. test is a This"
# a=sample.split()
# b=[]
# for i in a:
#     c=a.count(i)
#     b.append(c)
# d=zip(a,b)
# print(dict(d))



# a=300
# b=50
# c=70
# if a>b and a>c:
#     print("a is gre")
# elif b>a and b>c:
#     print("b is gre")
# else:
#     print('c is gre')


# a=2
# b=3
# c=7
# l=[]
# l.extend([a,b,c])
# l.reverse()
# print(l)


# num = 10
# a,b = 0, 1
# print("Fibonacci Series:", a, b, end=" ")
# for i in range(2, num):
#     c = a + b
#     a = b
#     b = c
#     print(c, end=" ")
# print()


# num = 145
# temp = num
# sum = 0
# while num > 0:
#     fact = 1
#     rem = num % 10
#     for i in range(1, rem + 1):
#         fact *= i
#     sum += fact
#     num //= 10
# if sum == temp:
#     print("Yes,", temp, "is a strong number.")
# else:
#     print("No,", temp, "is not a strong number.")


# for num in range(1,101):
#     if num > 1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num,end=',')

a=[2,5,1,3]
# print(max(a))
a.sort()
print(a[-1])



