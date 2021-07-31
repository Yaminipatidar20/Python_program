class Student:
    def get_data(self):
        self.rollno=input("Enter student Roll no:-")
        self.name=input("Enter student Name:-")
        self.age=eval(input("Enetr student Age:-"))
    def show_data(self):
        print("Roll no:-",self.rollno)
        print("Name:-",self.name)
        print("Age:-",self.age)
class Test(Student):      #single inheritance
    def get_marks(self):
        self.sub1=eval(input("Enter marks of sub1:-"))
        self.sub2=eval(input("Enter marks of sub2:-"))
        self.sub3=eval(input("Enter marks of sub3:-"))
        #self.sub4=eval(input("Enter marks of sub4:-"))
    def put_marks(self):
        print("Marks of subject 1:-",self.sub1)
        print("Marks of subject 2:-",self.sub2)
        print("Marks of subject 3:-",self.sub3)
        self.total=self.sub1+self.sub2+self.sub3
class Result(Test):           #multilevel inheritance
    def display(self):
        self.total=self.sub1+self.sub2+self.sub3
        self.per=self.total/3
        print("Total Marks:- ",self.total)
        print("percantage:-",self.per)
r1=Result()
r1.get_data()
r1.get_marks()
r1.show_data()
r1.put_marks()
r1.display()