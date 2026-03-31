"""
Write a Python program using OOP to create a class Student with attributes name, roll_no, and marks.
 Add a method display() to print student details and a method result() that prints 'Pass' if marks >= 40 else 'Fail'.
 Create two student objects and call both methods.
"""


class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"name = {self.name}")
        print(f"Roll_no = {self.roll_no}")
        print(f"Marks = {self.marks}")

    def result(self):
        if(self.marks>=40):
            print("pass")
        else:
            print("fail")


studentobj = Student("mia Kalifa ",1,95)
studentobj.display()
studentobj.result()


studentobj = Student("Dani daniels",2,100)
studentobj.display()
studentobj.result()