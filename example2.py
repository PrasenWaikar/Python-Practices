class Hero:
    def __init__(self):
        self.name="aditya"
        self.place="hyd"
        self.age=34
    def dance(self):
        print("hero is dancing")
    def sleep(self):
        print("hero is sleeping")
h=Hero()
print(h.name)
print(h.place)
h.dance()
h.sleep()
h.name="srk"
h.movie="ddlj"
print(h.name)
print(h.movie)