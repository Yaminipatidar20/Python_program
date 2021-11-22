class Student:
    count=0
    name="TCS"
    def __init__(self):
        #self.name="TCS"      #instance variable
        Student.count=Student.count+1
s1=Student()
s2=Student()
s3=Student()
s4=Student()
s5=Student()
print("The Number of Student:-",Student.count)
print("Name of Company:-",Student.name)
        
