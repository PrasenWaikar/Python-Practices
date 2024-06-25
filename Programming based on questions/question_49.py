#Define a class named American and its subclass NewYorker. 
class American:
    def printNationality(self):
        print("American")

class NewYorker(American):
    def printCity(self):
        print("New Yorker")

# Example usage:
american = American()
american.printNationality()

new_yorker = NewYorker()
new_yorker.printNationality()
new_yorker.printCity()
