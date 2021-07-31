class calculation1:
    def summation(self,a,b):
        return a+b
class calculation2:
    def multiplication(self,a,b):
        return a*b
class Derived(calculation1,calculation2):
    def divide(self,a,b):
        return a/b
d=Derived()
print("Sum of Two Number:-",d.summation(10,20))
print("Multiplication of Two number:-",d.multiplication(10,20))
print("Division of Two Number:-",d.divide(10,20))


