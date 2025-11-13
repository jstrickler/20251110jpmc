colors = []   # same as colors = list()
fruits = list()
airports = list()
values = list()

# Class --> instance
x = 5  #  x = int(5)
b = "bat"  # b = str("bat")

fruits.append("mango")
fruits.append("guava")
fruits.append("soursop")
fruits.insert(0, "banana")
print(fruits.index("guava"))

class Dog:  #  CustomerAccount  DatabaseConnection
    def bark(self):
        print("Woof! woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
d2.bark()
