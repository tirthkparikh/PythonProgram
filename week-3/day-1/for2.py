# for i in range(1,10,2):
#     print(i,end=" ")


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))


if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)