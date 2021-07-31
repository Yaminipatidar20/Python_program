class Animal:
    def Speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog Barking")
class Dogchild(Dog):                  #multilevel inheritance
    def eat(self):
        print("Eating Bread......")
d=Dogchild()
d.bark()
d.Speak()
d.eat()