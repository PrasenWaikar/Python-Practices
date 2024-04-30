class Student:
    def __init__(self):
        self.name="sampada"
        self.email="joshi@gmail.com"
        self.phone=9422955920
        self.age=21
    def eat(self):
        print("student are eating")
    def study(self):
        print("student are studing")
s1=Student()
print(s1.name)
print(s1.email)
print(s1.phone)
print(s1.age)
s1.eat()
s1.study()

