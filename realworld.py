class Student:
    num_of_student=0     #class variable
    class_teacher="Nitesh Jain"
    def __init__(self):
        self.rollno=input("Enter Student Rollno:-")
        self.name=input("Enetr Student Name:-")
        self.marks=eval(input("Enter Students Marks:-"))
        self.age=input("Enter students Age:-")
        self.bgrp=input("Enter Students Blood Group:-")
        self.grade=""
        Student.num_of_student+=1
    def calcGrade(self):
        if self.marks>=80:
            self.grade="A+"
        elif self.marks>=70:
            self.grade="A"
        elif self.marks>=60:
            self.grade="B"
        elif self.marks>=50:
            self.grade="C"
        elif self.marks>=40:
            self.grade="D"
        else:
            self.grade="E"
    def show(self):
        print("Roll NO:-",self.rollno)
        print("Name:-",self.name)
        print("Marks:-",self.marks)
        print("Age:-",self.age)
        print("Blood Group:-",self.bgrp)
        print("Grade:-",self.grade)
stu1=Student()
stu2=Student()
stu3=Student()
stu4=Student()
stu1.calcGrade();
stu2.calcGrade();
stu3.calcGrade();
stu4.calcGrade();
print("Total number of student:-",Student.num_of_student)
print("The class teacher is:-",Student.class_teacher)
stu1.show();
stu2.show();
stu3.show();
stu4.show();
