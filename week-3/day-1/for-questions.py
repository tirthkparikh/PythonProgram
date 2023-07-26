a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

total=0
"""
thir value in for loop is step of incremeant or decremant

"""
for i in range(a,b+1,-1):
    total+=i
print(total)
