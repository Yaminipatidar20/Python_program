class Computer:
    def config(self,cpu,ram,hdd):
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd
    def show_config(self):
        print("Reference of object:-",self)
        print("CPU:-",self.cpu)
        print("RAM:-",self.ram)
        print("HDD:-",self.hdd)
c1=Computer()
c2=Computer()
#Computer.config(c1,'i3','4GB','1TB')
#Computer.config(c2,'i5','8GB','3Tb')
#Computer.show_config(c1)
#Computer.show_config(c2)
c1.config('i3','4GB','1TB')
c2.config('i5','8GB','3TB')
c1.show_config()
c2.show_config()
