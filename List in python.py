'''
l=[1,2,3,4,"Ravan",69.96,True,"hello"]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[5])
print(l[6])
print(l[-4])
print(l[len(l)-4])
if "Ravan" in l :
  print("yes")
else:
  print("no")

if 4 in l :
  print("yes")
else:
  print("no")
  '''

  #slicing can also be done in list
'''
animals = ['cat','dog','bat','mouse','pig','horse']
print(animals)
print(animals[0:4])
print(animals[0:])
# print(animals[0:5:2])
print(animals[-8:-1:2])
'''

#list comprehension...
'''
lst=[i for i in range(1,21) if i % 2 == 0]
print(lst)


#list methods
# reverse
# index
# count

l=[1,2,4,6,8]
l.append(3)
l.insert(2,69)
print(l)

l2=[12,42,4,1,6,53]
l2.sort()
# l2.sort(reverse=True)
print(l2)

#extend
p=["a",'b','c','d']
q=[1,2,3,4]
print(p)
print(q)
p.extend(q)
print(p)
#concatinate list
y=[1,2,3,4]
z=["p","o","i"]
x=y+z
print(x)
'''