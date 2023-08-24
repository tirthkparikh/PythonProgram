#scoping


a=100
def total():
 
    print(id(a))
    b=20
    total=a+b
    print(total)
total()
print(id(a))
print(a)    