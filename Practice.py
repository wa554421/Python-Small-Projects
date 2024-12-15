# class waleed:
#     def __init__(self):
#         pass
#     def hello(self):
#         print("Hello")
# call=waleed()
# #del call # using Del to delete object
# call.hello()

# class private:
#     def __init__(self,email,password):
#         self.email=email
#         self.__password=password # this __ gives a privete attribute so we cant directly access this attrubute outside the class but i use this on another or inside the class

#     def print(self):
#         print(self.email)
#         print(self.__password)

# emai=input("Enter Email : ")
# cal=private(emai,"hello")
# print(cal.email)
# cal.print()


class person:
    __name="Waleed Ahmed" # This __ use to make private attribute (cant directly access ouside the class and easily access inside the class)

    def __waleeds(self): #This function name is private so cant access outside the class and it used only inside the class and another function of class
        print("Waleed")
    
    def welcome(self):
        self.__waleeds()

calll=person()
# print(calll.__name)
calll.welcome()



#2nd Method Encapsulation
#Encapsulation means keeping the details of an object hidden and only exposing what’s necessary. It protects data by using private variables and methods, which can only be accessed or modified through public methods.


# 3rd Pillar (INHERITANCE)
#Inheritance is when one class (child) takes on the properties and behaviors of another class (parent).

#4th Polymorphism:
# Polymorphism means "many forms". In Python, it allows you to use the same method or function name for different objects, and each object can behave differently when that method is called.
#fro exapple + is used in differnt places in differnt working 1+2 or [1,2]+[2,7] add the list

# Inheritance Using Praent class (attributes and methods) to child class
# Parent class
#Single Inheritance
class inheri:
    def start(self):
        print("This Car is Start ! ")
    def well(self):
        print("This is Well")

# Child class
class car(inheri):
    def __init__(self,name):
        self.name=name

call=car("1")
call.start()

# Grand Child class
#Multi-Level Inheritance
class multi(car):
    def __init__(self):
        pass
s1=multi()
s1.well()
s1.well()

# Multiple Inheritance
# many Parent classes make and use this parent class to one child class at a same time
# Parent class
class a:
    def c(self):
        print("this is 1st parent cell")
# Parent class
class b:
    def d(self):
        print("This is a 2nd Parnet Cell")
# Child Class
class chil(a,b):
    def __init__(self):
        pass

ca=chil()
ca.c()
ca.d()


#Types of Inheritance
#Single Inheritance
#Multi-Level Inheritance
# Multiple INheritance






# Tip: Using class is good becuase again again call class usign differnet objects name 
nem=input("Enter a house Name :")
call1=car(nem)
call1.start()