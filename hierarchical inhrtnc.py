class Animal(object):
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name,"Says",self.sound())
class Cow(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
        print("This is Cow Class")
    def sound(self):
        return "moo"
class Horse(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
        print("This is Horse Class")
    def sound(self):
        return "neigh"
class Sheep(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
        print("This is Sheep Class")
    def sound(self):
        return "baaaaa"
s=Horse("Chetak")
s.speak()
c=Cow("Rambha")
c.speak()
Sheep("Mithi").speak()
