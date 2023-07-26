"""
we take input from user to run some codes
input()=>this fn helps in taking input from user
by default type of input is str
"""
a = input()
print(type(a))
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))
d = int(input("Enter your fourth number: "))


print(f"addition of {a},{b},{c} and {d} is {a+b+c+d}")
