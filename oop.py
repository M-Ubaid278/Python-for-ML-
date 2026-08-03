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


class Bank:

    def __init__(self, balance, account_No):
        print("Welcome to the bak services")
        self.balance=balance
        self.account=account_No

    def debit(self,amount):
        self.balance -=amount
        print("Total amount that is debited:", amount)

    def credit(self, amount):
        self.balance += amount
        print("amount to be add:", amount)

    def total_Balancce(self ):
        print("Total amount :" , self.balance)

u1=Bank(12343,1)
print(u1.balance,u1.account)

u1.debit(0)

u1.credit(28282)

u1.total_Balancce()
        