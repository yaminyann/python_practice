class Vehicle:
    """base class for all vehicle""" # this is docstring
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("driving",self.manufacturer,self.name)

    def turn(self,direction):
        print("turnning",self.name, "to ", direction)

    def brake(self):
        print(self.name, "is stoping ")


class Car(Vehicle):
    """car class"""
    def __init__(self,name,manufacturer,color,year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4
        print("A new car has been created . Car name is :",self.name)
        print("It has ",self.wheels,"Wheels")
        print("The car was Build ",self.year)

    def change_gear(self,gear_name):
        """methood for changing gear"""
        print(self.name,"is changing gear to ",gear_name)


if __name__ == "__main__":
    c = Car("Mustang 5.0 GT coupe ","ford","red",2017)



if __name__ == "__main__":
        v1 = Vehicle("Fusion 110EX ","walton","black")
        v2 = Vehicle("Softal delux ","harley devaidson","blue")
        v3 = Vehicle("Mustang 5.0 GT cuope", "ford", "red")

        v1.drive()
        v2.drive()
        v3.drive()

        v1.turn("left")
        v2.turn("right")

        v1.brake()
        v2.brake()
        v3.brake()
        c = Car("mustang gt coupe ","ford","red")
        c.drive()
        c.brake()
        c.change_gear("park")


            """methood overridding"""


class Vehicle:
    """base class for all vehicle"""
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self,direction,signal):
        print("Turning", self.name, "to", direction,"signal is",signal)

class Car(Vehicle):
    """car class"""
    def __init__(self,name,manufacturer,color,year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4

    def change_gear(self,gear_name):
        """methood for changing gear"""
        print(self.name,"is chaning geear to ",gear_name)

    def turn(self,direction,signal):
        print(self.name, "is turnning ", direction,"siganal are ",signal)

if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe","ford","red",2017)
    v = Vehicle("softtail delux ", "harley devidson", "blue")
    c.turn("right","red")
    v.turn("left","yellow")


class Vehicle:
    """base class for all vehicle"""
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self,direction,signal):
        print("Turning", self.name, "to", direction,"signal is",signal)

class Car(Vehicle):
    """car class"""
    def __init__(self,name,manufacturer,color,year):
        print("creating a car ")
        super().__init__(name,manufacturer,color)
        self.year = 2017
        self.wheels = 4

    def change_gear(self,gear_name):
        """methood for changing gear"""
        print(self.name,"is chaning geear to ",gear_name)

    def turn(self,direction,signal):
        print(self.name, "is turnning ", direction,"siganal are ",signal)

if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe","ford","red","2017")
    print(c.name,"\n",c.year,"\n",c.wheels)
