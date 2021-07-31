class Employee:
    __count=0                        #Abstract variable
    def __init__(self):
        Employee.__count=Employee.__count+1;
    def display(self):               #abstract method
        print("The number of Employees",Employee.__count)
emp=Employee()
emp2=Employee()
try:
    print(emp.__count)
finally:
    emp.display()

