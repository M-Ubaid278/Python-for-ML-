# class book:
#      def __init__(self, book_id, title, author, available):
#           self.book_id=book_id
#           self.title=title
#           self.author=author
#           self.available=available
     
#      def show_details(self):
        
#           print("Book_id:",self.book_id)
#           print("Title:", self.title)
#           print("Author:",self.author)
#           print("Available:",self.available,"\n")


# class library:
#      def __init__(self ):
#           self.library_Name="XYZ"
#           self.books=[]

#      def add_books(self,book):
#           self.books.append(book)

#      def show_books(self):
#           for book in self.books:
#             book.show_details()

#      def borrow_book(self,Book_id):
#           for book in self.books:
#                if(book.book_id==Book_id):
#                 if(book.available=='True'):
#                     book.available=False
#                     print("Book borrowed successfully")
#                 else:
#                     print("Book is not available")
#                else:
#                    print("Book_id is not a valid:try again")




# lib=library()

# while True:
#      book_id=str(input("Enter your book id:"))
#      title=str(input("Enter title:"))
#      author=str(input("Enter author:"))
#      available=bool(input("Enter the availibility:"))

#      b=book(book_id,title,author,available)
    
#      lib.add_books(b)
     
#      check=str(input("Do you want to enter more book:y/n  :"))
#      if(check=="n"):
#           break
# print("\n --------BOOK DETAILS----------")

# lib.show_books()
# lib.borrow_book("B102")          

# list1=[1,2,3,4,5]
# list2=[5,6,7,8,9]

# new_list=[]

# for i in range(0,len(list1)):
#     x=list1[i] * list2[i]
#     new_list.append(x)

# print(new_list)

# import numpy as arr
# print("Enter the data:")
# arr1=arr.zeros(5,dtype=int)
# i=0
# while i < 5:
#     n=int(input())
#     arr1[i]=n
#     i +=1
    
# print(arr1)

# -------------------------- one function with the value entered by the user------------------------------------


# import numpy as np
# print("Enter num:")
# arr=  np.ones((2,3,4) , dtype=int)

# for i in range(2):
#     for j in range(3):
#         for k in range(4):
#             n=int(input())
#             arr[i][j][k]=n
    

# print(arr)

# import numpy as np 
# print(np.full((2,3,4),2,dtype=int))

import numpy as np 
# print(np.arange(10,100,10,dtype=int))

# print(np.eye(5,3, dtype=bool))

# print(np.linspace(10,30,2))

# print(np.random.rand(4,2))
# print(np.random.randn(4))

# print(np.random.randint(10,30 ,(2,2)))

# print(np.random.normal(4,2,(5)))

pro=np.random.randint(10,30 ,(2,2))
print(pro)
print(pro.ndim)
print(pro.size)
print(pro.shape)
print(pro.dtype)
