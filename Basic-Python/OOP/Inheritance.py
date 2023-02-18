import random

class Animal:
    info = "A living organis, that feeds on organic matter"

    def __init__(self, name):
        print("An animal is created")
        self.name = name

class Dog(Animal):  #Name in square brakets means parent of the class
    info = "a domesticated carnivorous mammal that typically has a long snout"

    def __init__(self, name):   #argument name is necessary due to parent.
        super().__init__(name)
        print("A dog is created")
        self.lucky_number = random.randint(1,10)
        self.fur = ""


    def bark(self):
        print(f"Wolf! My name is {self.name} and my number is {self.lucky_number}")

class Bulldog(Dog): #Name in square brakets means parent of the class

    def __init__(self,name):
        super().__init__(name)
        print("A Bulldog is created")

class Pet(Bulldog): #Name in square brakets means parent of the class

    def __init__(self,name):
        super().__init__(name)
        print("It is my pet")


dog1 = Pet("Fido")
dog1.bark()

''' dog1 = Dog("Fido")
#dog2 = Animal()

#print(dog2.info)
print(dog1.info) '''

