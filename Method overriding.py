
class Parent():

    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)


class Child(Parent):

    def __init__(self):
        self.value = "Inside Child"

    def show(self):
        print(self.value)


obj1 = Parent()
obj1 = Child()

obj1.show()
# obj1.show()
