class RBI:
    def getroi(self):
        return 7;
class SBI(RBI):
    def getroi(self):
        return 6.5;
class BOI(RBI):
    def getroi(self):
        return 7.2;
class BOB(RBI):
    def getroi(self):
        return 7.6;
class ICICI(RBI):
    def getroi(self):
        return 7.9;
b1=RBI()
b2=SBI()
b3=SBI()
b4=BOB()
b5=ICICI()
print("RBI Rate of Interest:-",b1.getroi())
print("SBI Rate of Interest:-",b2.getroi())
print("BOI Rate of Interest:-",b3.getroi())
print("BOB Rate of Interest:-",b4.getroi())
print("ICICI Rate of interest:-",b5.getroi())
