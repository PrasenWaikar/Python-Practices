class one:
    def show(self):
        print(f"Multiplications is : {self.p}")

class two(one):
    def product(self,a,b):
        self.p=a*b

class three(two):
    def product(self,a,b,c):
        self.p=a*b*c

t=two()
t.product(11,10)
t.show()