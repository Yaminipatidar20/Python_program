class A:
    def __init__(self):
        print("Init of class A")
    def feature1(self):
        print("Feature 1 of class A")
    def feature2(self):
        print("Feature 2 of Class A")

class B():
    def __init__(self):
        #super().__init__()
        print("Init of class B")
    def feature1(self):
       # A.feature1(self)
        super().feature1()
        print("Feature 1 of class B")
    def feature3(self):
        print("Feature 3 of Class B")
class C(B,A):
    def __init__(self):
        #super().__init__()
        A.__init__(self)
        B.__init__(self)
        print("Init of class C")
obj=C()
#obj1=B()
#obj1.feature1()
#obj1.feature2()
#obj1.feature3()

