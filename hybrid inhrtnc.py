class Student:
    def getdata(self):
        self.rollno=input("Enter Roll No. of Student:-")
        self.name=input("Enter Name of Student:-")
        self.age=eval(input("Enter Age of Student:-"))
    def putdata(self):
        print("Roll No. of Student:-",self.rollno)
        print("Name of Student:-",self.name)
        print("Age of Student:-",self.age)
class test(Student):
    def getmarks(self):
        self.sub1=eval(input("Enter Marks of BDA:-"))
        self.sub2=eval(input("Enter Marks of SEM:-"))
        self.sub3=eval(input("Enter Marks of DS:-"))
    def putmarks(self):
        print("Marks of BDA:-",self.sub1)
        print("Marks of SEM:-",self.sub2)
        print("Marks of DS:-",self.sub3)
class Sports:
    def getscore(self):
        self.score=eval(input("Enter Sports Wt.:-"))
    def putscore(self):
        print("Sports Wt:-",self.score)
class Result(test,Sports):             #hybrid inheritance
    def display(self):
        self.total=self.sub1+self.sub2+self.sub3+self.score;
        self.per=self.total/4.0;
        self.putdata()
        self.putmarks()
        self.putscore()
        print("Total Marks:-",self.total)
        print("Percentage:-",self.per)
S=Result()
S.getdata()
S.getmarks()
S.getscore()
S.display()