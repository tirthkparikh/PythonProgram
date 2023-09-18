"""
Create a class Student

Create method setData and ask for name,phy,sci,eng,hind,math
Create method display and display all details
Create method totalMarks and display total marks (total - local variable)
Create method totalMarks2 and return total marks (total - local variable)
Create method updateName, enter your new name, then call display()
"""
class Student:
    def setData(self):
        self.name = input("Enter your name:  ")
        self.marks= list(map(int,input("enter 5 subject marks:  ").split()))
        [self.phy,self.maths,self.chem,self.eng,self.ss]=self.marks
        

s1=Student()
s1.setData()
