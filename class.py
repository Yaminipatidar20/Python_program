class Car:
    def getdata(self,modelname,year):
        self.modelname=modelname
        self.year=year

    def display(self):
        print(self.modelname,self.year)
c1=Car()
c1.getdata("Toyota",2016)
c1.display() 
    
    
