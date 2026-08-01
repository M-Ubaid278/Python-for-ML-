
with open("practice.txt","w") as d:
    
    print("Enter numbers:")
    i=0
    while i<10:
        n=(input())
        d.write(n + "\n")
        i +=1

print(" ")
print("Get the output from the file")
with open("practice.txt","r") as d:
    count=0
    for i in d:
     if(int(i)%2==0):
        count +=1

    print(count)

