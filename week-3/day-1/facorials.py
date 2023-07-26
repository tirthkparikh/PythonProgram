a=int(input("Enter the first number: "))
b=True
for i in range(2,int(a**(1/2)+2)):
    if a%i==0:
        b=False
        break
print(b)
