# str1= "This is all about the strings"
# char= str1[19]
# print(len(str1))

# print(char)
# print(str1[20])



# first_Name=input("Enter first's name:")
# cap= first_Name.capitalize()
# print("Length:", cap,"\n" ,len(first_Name))

# con=input("Enter the letter to find the position:")
# print(first_Name.count(con))


# marks=int(input("Enter your marks:"))

# if(marks > 90):
#     print("A")

# elif( marks > 80 and marks < 90):
#     print("B")

# elif(marks >70  and marks < 80):
#      print("C")
# else:
#     print("D")


# num=int(input("Enter num:"))

# if(num % 7==0):
#     print("Number is divisble by 7")

# else:
#     print("Number is not ")

# name="Ubaid"
# name1="Zahid"

# full_name= f"{name} {name1}"
# print(full_name)

# name="Ubaid"
# name1="Zahid"

# full_name= f"{name} {name1}"
# print( f"hello,  {full_name.title()}!")


# name="Ubaid"
# name1="Zahid"

# full_name= f"{name} {name1}"

# message= f"Hello, {full_name.title()}! How are you?"
# print(message)                                   

# list=[1, "abc", "abd",1]
# list1= list.copy()
# rev= list1.reverse()
# if(list==rev):
#     print("list is palindrome ")
# else:
#     print("list is not a palindrome")

# print(list)

student_Id="F2024266193"
membership=True
book_borrowed=4
fine=0

check_studentId=input("Enter Id:")

if(check_studentId[0]=="F"):

    if(check_studentId==student_Id):
        print("Id is valid")

        if(membership==True):
            print("Member")

            if(book_borrowed < 5):
             print("You are eligible for getting a new book")

             if(fine == 0):
                 print("No pending dues")   

                 print("All conditions are statisfied and now you can get a new book")

             else:
                 print("Pay you previous pending dues")

            else:
                print("You are not eligible")

        else: 
             print("You are not member")

    else:
         print("enter id is not matched")

else:
        print("Id is invalid")
        