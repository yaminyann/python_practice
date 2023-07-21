# class Car:
#     name = "Rols Royls"
#     color = "black"
#
#     def start():
#         print("starting the engine")
#
# print("name of the car ",Car.name)
# print("color is ",Car.color)
# Car.start()


# class Car:
#     name = "premio"
#     color = "white"
#
#     def start():
#         print("starting the engine")

# print("name of the car ",Car.name)
# print("color is ",Car.color)
# Car.start()
# print(dir(Car))


# create a object

# class Car:
#     name = ""
#     color = ""
#
#     def start():
#         print("starting the engine")
#
# myCar = Car()
# myCar.name = "Axio"
# print(myCar.name)
# myCar.start()

# class Car:
#     name = ""
#     color = ""
#
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     def start(self):
#         print("starting the engine")
#
# myCar = Car("BUggatti","gray")
#
# print(myCar.name)
# print(myCar.color)
# myCar.start()

# class Car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c
#     def start(self):
#         print("starting the engine")
#
# myCar = Car("Axio","white")
# print(myCar.name)
# print(myCar.color)
# myCar.start()


# class Car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c
#
#     def start(self):
#         print("name  ",self.name)
#         print("color ",self.color)
#         print("starting the enginee")
#
# myCar = Car("Premio","red")
# myCar.start()

# class Car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c
#
#     def start(self):
#         print("name  ",self.name)
#         print("color ",self.color)
#         print("starting the enginee")
#
# myCar_one = Car("Premio","red")
# myCar_one.start()
# myCar_two = Car("Axio","White")
# myCar_two.start()




class Car:

    def __int__(self,n,mf,c,cy,cc):
        self.name = n
        self.manuf = mf
        self.color = c
        self.c_y = cy
        self.cc = cc


    def start(self):
        print("starting the enginee")

    def brak(self):
        print("Break the car")

    def drive(self):
        print("drive the car ")

    def turn(self):
        print("Turn left on the car")

    def chage_gear(self):
        print("Change the gear at Neutal")


myCar = Car()
myCar.cc = 1200
myCar.name = "bugatti"
myCar.color = "Yellow"
print(myCar.cc,myCar.color,myCar.name)
myCar.start()
myCar.brak()
myCar.drive()
myCar.turn()
myCar.chage_gear()