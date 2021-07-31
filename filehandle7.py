import pickle as p
class Student:
    def __init__(self,rno=0,name=""):
        self.rollno=rno
        self.name=name
        self.sub1,self.sub2,self.sub3=0,0,0
        self.total,self.per=0,0
    def readMarks(self):
        print("Enter Marks of 3 Subjects")
        self.sub1=eval(input("Enter Marks of Subjects 1:-"))
        self.sub2=eval(input("Enter Marks of Subjects 2:-"))
        self.sub3=eval(input("Enter Marks of Subjects 3:-"))
    def display(self):
        print("Student Details are:-")
        print("Roll Number:-",self.rollno)
        print("Name :-",self.name)
        print("Marks of Subject 1:-",self.sub1)
        print("Marks of Subject 2:-",self.sub2)
        print("Marks of Subject 3:-",self.sub3)
        self.total=self.sub1+self.sub2+self.sub3;
        self.per=self.total/3;
        print("Total Marks:-",self.total)
        print("Percantage:-",self.per)
stu1=Student(101,"Amit")
stu2=Student(102,"Ankur")
fout=open("Studentrecord.dat","wb")
stu1.readMarks();
stu2.readMarks();
p.dump(stu1,fout);
p.dump(stu2,fout);
fout.close()
stu=Student()
fin=open("Studentrecord.dat","rb")
try:
    while True:
        stu=p.load(fin)
        stu.display()
except EOFError:
    fin.close()


