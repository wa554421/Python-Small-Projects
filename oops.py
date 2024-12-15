class waleed:
    # # Default Constructor (if you not make so python automatically make this)
    # def __init__(self):
    #     self

    #only one time stores in memory
    college="Scholars" #Class Atribute
    name="Anonymous"
    def __init__(self,name,health,damage,speed): # Paremetirized Constructor Init function
        print("Showing")
        self.name=name # Object Attributes
        self.health=health # The data that is stored inside the class is called attributes
        self.damage=damage
        self.speed=speed

    def waleed2(self):
        print("Hello")
        return self.damage

obj=waleed("Waleed",12,23,23)
print(obj.health)
print(obj.college)
print(obj.waleed2())


#Static method
class shah:
    def __init__(self):
        pass
    @staticmethod # Decorator(Changing the behaviour to the normal function)
    def taleeb():
        print("Asalam u Alaikum")

shah1=shah()
shah1.taleeb()

# Important Things

# Abstraction (Hiding the Implementation details of a class)

# class Car:
#     def __init__(self):
#         self.acc=False
#         self.clutch=False
    
#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("Car Started !")

# cal=Car()
# Car.start()

class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car Started !")

my_car = Car()
my_car.start()


# ENCAPSULATION (wRITNG DATA AND FUMCTIONS IN A SINGLE UNIT)


# class waleed:
#     name="Waleed"
#     clas=1
# obj1=waleed
# print(obj1.clas)