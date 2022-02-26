class mobile:
    def __init__(self):
        self.name="Redmi"
        self.rom="128GB"
        self.ram="2GB"
        self.proceesor="AMD"

    def configuration(self):
        print("mobile name:- ",self.name)
        print("mobile rom is:- ",self.rom)
        print("mobile rom is:-",self.ram)
        print("mobile proceesor:- ",self.proceesor)

mb=mobile()
mb.configuration()
print("-----------------------------------update values--------------------------------------------")
mb.name="Redmi7A"
print("updated:-",mb.name)
#mb.configuration()
