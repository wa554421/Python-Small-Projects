#Multi-Level-Inheritance
# this is a chain parent tochild parent to child and long chain are connected
class s1:
    def __init__(self):
        pass

    def waleed(self):
        print("This is First Praent cell")

class s2(s1):
    def __init__(self):
        pass
    def start(self):
        print("Starting")

class s3(s2):
    def __init__(self):
        pass

call=s3()
call.waleed()

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

# Super Method
class parent1:
    def __init__(self,name):
        self.name=name
    def p1(self):
        print("Printing")
    def p2(self):
        print("Printing 2")

class child1(parent1):
    def __init__(self,name):
        super().__init__(name) #tHIS Super Function helps to reach the ttributes inside the parent class (because mostly work on reaching the direct function and attributes problem so this helps this)
        

c=child1("wALEED")
print(c.name)


# Class Method
class clas:
    name="Anonymous"
    def __init__(self):
        pass
        

    @classmethod # used to chnage the class attributes 
    def meth(cls,name):
        cls.name=name

caly=clas()
print(caly.name)

    
call4=clas("wALEEDS")
print(call4.name)


# property 
class wahka:
    @property  # This Property changes this function to attribute
    def wal(self):
        print("Hello")