# class waleed:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def avg(self):
#         sums=sum(self.marks)
#         avg=sums/len(self.marks)
#         print(f"{self.name} your avergae marks is {avg}")



# # Using Input
# name=input("Emter a Name : ")
# mark1=int(input("Enter a Marks of English : "))
# mark2=int(input("Enter a Marks of Urdu : "))
# mark3=int(input("Enter a Marks of Science : "))


# call=waleed(name,[mark1,mark2,mark3])
# call.avg()

# class  bank:
#     def __init__(self,number,no):
#         self.account_no=no
#         self.nymbe=number

# call=bank(23,657)
import os
import time 

class newclass:

    school_name="Gandhara Public School"
    def __init__(self,name,clas,marks):
        self.name=name
        self.clas=clas
        self.marks=marks

    def typewriter(self, text, delay=0.006):
        """Typewriter effect for displaying text"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # Move to the next line

    def printing(self):
        all=300
        totalmarks=sum(self.marks)
        final=totalmarks/all*100
        finals=round(final,2) # Round off the Percenyage vlaue means removing the longest value after the zero
        self.typewriter(f"************************************ {self.school_name} ********************************************")
        self.typewriter(f"Name : {self.name}")
        self.typewriter(f"Overall Percentage : {finals} %")
        self.typewriter(f"Emglish Marks : {self.marks[0]}")
        self.typewriter(f"Urdu Marks : {self.marks[1]}")
        self.typewriter(f"Computer Marks : {self.marks[2]}")
        self.typewriter("*****************************************************************************************************")

name=input("Enter Your Name : ")
grade=int(input("Enter Your Class/Grade : "))
marks1=int(input("Enter a Marks of English : "))
marks2=int(input("Enter a Marks of Urdu : "))
marks3=int(input("Enter a Marks of Computer : "))

os.system('cls' if os.name == 'nt' else 'clear') # Clear the input/Terminal screen before showing (output/Calling function in class)


cal=newclass(name,grade,[marks1,marks2,marks3])
cal.printing()
        