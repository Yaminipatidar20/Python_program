class Animal:
    def Speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog Barking")
d=Dog()
d.bark()
d.Speak()