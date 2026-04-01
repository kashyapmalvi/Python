"""
Design a Python class hierarchy for a Library Management System.
 Create a base class Book with attributes title, author, and price. 
 Derive a class EBook that adds a file_size attribute. Implement a method display_info() in both classes. 
 Demonstrate inheritance and method overriding with at least two objects.
"""
class Books:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display_info(self):
        print(f"Title is {self.title}")
        print(f"author is {self.author}")
        print(f"price is {self.price}")


class EBook(Books): 
  
    def __init__(self,title,author,price,size):
        super().__init__(title, author, price)
        self.size = size


    def display_info(self):
        super().display_info()
        print(f"file size = {self.size}")



miakalifa = Books("Bigbons","Mia Kalifa",100)
miakalifa.display_info()


Dani = EBook("BigBons","Dani",100,50)
Dani.display_info()