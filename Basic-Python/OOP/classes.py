import random 

class Dog:
    info = "A domesticated carnivorous mammal"

    def __init__(self,name,age):
        print("I am alive!")
        self.lucky_number = random.randint(1,100)
        self.name = name
        self.age = age
        
dog1 = Dog("Rodolf",20)
dog2 = Dog("Ketty",25)

#print(dog1.lucky_number)
#print(dog2.lucky_number)

#dog1.name = "Lukas"

#print(dog1.name + " and " + dog1.age)
#print(dog2.name + " and " + dog2.age)
print(dog1.name)
print(dog2.name)
print(dog1.age)
print(dog2.age)
print(dog1.lucky_number)
# print(dog3.name) name attribute is only creatred to previous object.

