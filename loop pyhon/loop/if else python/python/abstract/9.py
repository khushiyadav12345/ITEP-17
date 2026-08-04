# 9. Library Management

# Parent:

# LibraryItem

# Derived:

# Book
# Magazine
# Newspaper

# Implement borrowing system.

class LibraryItem:
    def borrowing(self):
        pass
    
class Book(LibraryItem):
    def borrowing(self):
        print("Book borrowed")
        
class Magazine(LibraryItem):
    def borrowing(self):
        print("Magazine borrowed")
        
class Newspaper(LibraryItem):
    def borrowing(self):
        print("Newspaper borrowed")
        
b = Book()
b.borrowing()

m = Magazine()
m.borrowing()

n = Newspaper()
n.borrowing()
        
    