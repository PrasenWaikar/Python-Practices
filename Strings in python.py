string = "a for apple b for banana\nc for catwomen"
name = "prasen"
friend = "mau"
print(string)
print("hello",name)
print("hello",friend)

print(friend[0])
print(name[3])
print(string[4])
print(friend[2])

sample = "qwertyuiopasdfghjklzxcvbnm"
for char in sample :
  print(char)

  # Strings Slicing and Operations on Strings

  name = "prasen"
  length = len(name)
  print("you name is of ", length , "characters")
  print(name[2])
  print(name[1])
  print(name[0])
  print(name[0:4])
  print(name[:3])#automatically takes zero at first
  print(name[-2])
  a= "harpy"
  print(a[-4:-2])

  # String Methods(there are alot of methods some of them are below)
  # note strings are immutable...once string written cannot be change...changes can only include upper/lower etc

  name = "praSen"
  print(name.upper())
  name1 = "PRASEENNnN"
  print(name1.lower())
  print(name.replace("praSen","batman"))
  name2 = "Hello world this is the end"
  print(name2.split())   #SPLIT WILL CONVERT STRING INTO LIST
  name3 = "prasen is batman and batman is prasen"
  print(name3.count("batman"))
  print(name3.find("batman"))

  