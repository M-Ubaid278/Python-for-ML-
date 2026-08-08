class book:
     def __init__(self, book_id, title, author, available):
          self.book_id=book_id
          self.title=title
          self.author=author
          self.available=available
     
     def show_details(self):
        
          print("Book_id:",self.book_id)
          print("Title:", self.title)
          print("Author:",self.author)
          print("Available:",self.available,"\n")


class library:
     def __init__(self ):
          self.library_Name="XYZ"
          self.books=[]

     def add_books(self,book):
          self.books.append(book)

     def show_books(self):
          for book in self.books:
            book.show_details()

     def borrow_book(self,Book_id):
          for book in self.books:
               if(book.book_id==Book_id):
                if(book.available=='True'):
                    book.available=False
                    print("Book borrowed successfully")
                else:
                    print("Book is not available")
               else:
                   print("Book_id is not a valid:try again")




lib=library()

while True:
     book_id=str(input("Enter your book id:"))
     title=str(input("Enter title:"))
     author=str(input("Enter author:"))
     available=bool(input("Enter the availibility:"))

     b=book(book_id,title,author,available)
    
     lib.add_books(b)
     
     check=str(input("Do you want to enter more book:y/n  :"))
     if(check=="n"):
          break
print("\n --------BOOK DETAILS----------")

lib.show_books()
lib.borrow_book("B102")          
