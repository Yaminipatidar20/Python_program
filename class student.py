class Student:
    def getdata(self):
        self.rollno=input("Enter roll no. of student:-")
        self.name=input("Enter name of student:-")
        self.per=eval(input("Enter percantage of student:-"))
    def show_data(self):
        print("Roll no of student:-",self.rollno)
        print("Name of student:-",self.name)
        print("percantage of student:-",self.per)
s1=Student()
s2=Student()
s1.getdata();
s2.getdata();
s1.show_data();
s1.show_data();
print("s1 object:-",s1)
print("s2 object:-",s2)
