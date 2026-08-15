# import numpy as np
# arr=np.full(7,20)
# arr[3]=27
# arr[6]=31
# print(arr)

# import numpy as np
# print("Enter the total numbers you want to enter:", end="") 
# n1=int(input())
# arr=np.zeros(n1, dtype=int)
# sz=len(arr) 
# # print(sz)
# i=0
# print("Enter the numbers:")
# while i < n1:
#     n=int(input())
#     arr[i]=n
#     i +=1

# print(arr)
# print(arr.shape)
# print(arr.size)

import numpy as np
print("Enter the total students:", end="")
n=int(input())
arr=np.zeros(n, dtype=int)

i=0
print("Enter the student's marks:")
while i < n:
    n1=int(input())
    arr[i]=n1
    i +=1

print("FINAL MARKS OF", n , "STUDENTS:", arr)
print("Shape:", arr.shape)
print("SIZE:", arr.size)
print("DTYPE:",arr.dtype)

arr2=np.zeros((n,2),dtype=int)

print("Enter marks of two subjects:")
i=0
j=0

while i < n:
    j=0
    while j < 2:
        num=int(input())
        arr2[i][j]=num 
        j +=1
    i+=1

print(arr2)

student_ids=np.arange(1,n+1)
print("Student_Id:", student_ids)

space=np.linspace(0,100,5)
print("Lin-Space fun:", space)

arr3=np.eye(3,3)
print(arr3)

arr4=np.random.randint(0,100,(5))
print("Random values:",arr4)

arr5=np.random.randn(5)
print("Standard NP:",arr5)

print("Normal Dis:", np.random.normal(70,5,(5)))
