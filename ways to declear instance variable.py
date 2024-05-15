class demo:
    def __init__(self):
        self.a=10
        self.b=20
    def sample(self):
        print(self.a)
        self.x=99
d=demo()
d.c=30
print(d.a)
print(d.b)
print(d.c)
d.sample()
print(d.x)