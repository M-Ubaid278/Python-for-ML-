# class student:
#     name="Muhammad ubaidullah"
#     def __init__(self,name,pf,oop,dsa):
#         print("now move to the new concept:OOP")
#         self.name=name
#         self.Pf=pf
#         self.OOP=oop
#         self.Dsa=dsa

#     def avg(self):
#         avg= (self.Pf + self.OOP + self.Dsa) /3 
#         return avg


# s=student("Ubaid",45,89,99)
# print(s.name,s.Pf,s.OOP )
# print(s.avg())


# class Bank:

#     def __init__(self, balance, account_No):
#         print("Welcome to the bak services")
#         self.balance=balance
#         self.account=account_No

#     def debit(self,amount):
#         self.balance -=amount
#         print("Total amount that is debited:", amount)

#     def credit(self, amount):
#         self.balance += amount
#         print("amount to be add:", amount)

#     def total_Balancce(self ):
#         print("Total amount :" , self.balance)

# u1=Bank(12343,1)
# print(u1.balance,u1.account)

# u1.debit(0)

# u1.credit(28282)

# u1.total_Balancce()


# class student:
#     def __init__(self,name):
#         self.name=name

# s1=student("Ubaid")
# print(s1.name)

# del s1.name
# print(s1.name) give an error because it has alrady been deleted from the memory

#  -------------------------PRACTICE OF (INHERITANCE AND POLYMORPHISM)----------------------------------


# class CIRCLE:
#     def __init__(self,r):
#         self.radius=r

#     def area(self):
#         self.Area=pow(self.radius,2) * 3.14
#         print(self.Area)

#     def peri(self):
#         self.Peri= 2*3.14 *self.radius
#         print(self.Peri)
        

# a1=CIRCLE(4)
# a1.area()

# a2=CIRCLE(4)
# a2.peri()

# class Employee:
#     def __init__(self,role, department, salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def show_Details(self):
#         print( "role:",self.role,"\n","department:",self.department,"\n","Salary:", self.salary,"\n")

# class Engineer(Employee):
#     def __init__(self, name,age,role,department,salary):
#         self.name=name
#         self.age=age
#         super().__init__(role,department,salary)
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         self.show_Details()
        


# Emp1=Employee("Teacher","Cs",1234)
# Emp2=Employee("HOD","Cs",123433)

# Emp1.show_Details()
# Emp2.show_Details()

# emp3=Engineer("Software Engineer","Health", 153433,"XYZ",23)
# emp3.show()


class Order:
    def __init__(self, item, price):
        self.item=item
        self.price=price

    def __gt__(self, order):
        return self.price > order.price


item1=Order("cake",123)
item2=Order("Biskits",223)

print(item1 > item2)
        
