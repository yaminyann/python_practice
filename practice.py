
class Vehicle:
    def __init__(self,name,manufacturer,model,color,engine_cc,top_speed):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.engine_cc = engine_cc
        self.top_speed = top_speed
    def drive(self):
        print(self.name,"are running")

    def speed(self,speed):
        print(self.name,"running in speed ",speed)

    def brake(self):
        print(self.name,"is Stoping")


class MotorCycle(Vehicle):
    def __int__(self,name,manufacturer,model,color,engine_cc,top_speed,year):
        super().__init__(name,manufacturer,model,color,engine_cc,top_speed)
        self.year = year

    def gear(self,gear_number):
        print(self.name," gear is ",gear_number)

if __name__ == "__main__":
    v = Vehicle("rols royels","royle","royel-2.0","white",2500,250)
    b = MotorCycle("4v","apache","version4","balck",160,180)


    v.brake()
    b.gear(4)



