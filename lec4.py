# n=int(input("Enter number by user:"))

# sum=0
# for i in range(1, n+1):
#     sum +=i

# print(sum)

# n=int(input("Enter num:"))
# mul=1
# for i in range(n,1,-1):
#     mul *=i
# print(mul)

# n=int(input("Enter number:"))
# mul=1
# print("Table of", n)
# while mul<=10:
#     print( n, "*", mul, "=" , n*mul)
#     mul +=1


# nums=[1,4,9,16,25,36,49,36,49,64,81,100]
# n=49
# i=0
# for sq in nums:
#     if(n==sq):
#      print("Number is found",i)
#      continue
#     i =i+1


# nums=(1,4,9,16,25,36,49,64,81,100)
# # n=int(input("Enter number by the user to search in the tuple="))
# i=0
# n=36
# while i < len(nums):
#     if(n==nums[i]):
#         print("Number is present in the list")
#         break
#     else:
          
#         print("Number is not  present in the list")
          
    
#     i +=1

# n=int(input("Enter num:"))

# for i in range(1,11):
#     mul=n*i
#     print(mul)

rocks=[12,0,18,25,0,31,8,50]
sum_emp=0
sum_high=0
sum_norm=0

count_emp=0
count_high=0
count_norm=0
for i in range(len(rocks)):
    if(rocks[i]==0):
        sum_emp +=rocks[i]
        count_emp +=1
        print("Empty rock")
    elif(rocks[i]>30):
         sum_high +=rocks[i]
         count_high +=1
         print("High value rock")

    else:
         sum_norm +=rocks[i]
         count_norm +=1
         print("Normal rock")

print("\n")

print("Empty_rocks:",sum_emp)
print("high value_rocks:",sum_high)
print("Normal value_rocks:",sum_norm)

print("\n")

print("total Empty_rocks:",count_emp)
print("total high value_rocks:",count_high)
print("total Normal value_rocks:",count_norm)