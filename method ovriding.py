class Animal:
    def speak(self):
        print("Speaking")
class Dog(Animal):                         #method overriding
    def speak(self):
        print("Barking")
d=Dog()
d.speak()