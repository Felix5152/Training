class Inheritance:
    def walk(self):
        print("Run")

class Dog(Inheritance):
    def woof(self):
        print("Woof!")


class Cat(Inheritance):
    def meow(self):
        print("Meow!")
    

dog1 = Dog()
dog1.woof()
cat1 = Cat()
cat1.meow()

