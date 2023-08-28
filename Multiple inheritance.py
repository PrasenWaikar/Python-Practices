class mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

class father:
    fathername = ""
    def father(self):
        print(self.fathername)

class me:
    name = ""
    def name(self):
        print(self.name)

class son(mother,father):
    def parants(self):
        print("Father : ", self.fathername)
        print("Mother : ", self.mothername)
        print("My name : ",self.name)


m=son()
m.fathername = "Balasaheb"
m.mothername = "Priyanka"
m.name="Prasen"
m.parants()