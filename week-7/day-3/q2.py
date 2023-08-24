# Write a function prodDigits() that inputs a number and prints the product of digits of that number.
def prodDigits()->int:
    a=int(input(" "))
    product=1
    while a>0:
        c=a%10
        product=product*c
        a=a//10
    return product
print(prodDigits())



# def prodDigits():
#     num = int(input("Enter a number = "))
#     total = 1
#     for i in str(num):
#         total = total * int(i)
#     print(total)


# prodDigits()
prodDigits()

a=10
b=[1,2,3]
def s():
    print(a,id(a))
    print(a,id(b))
print(a,id(a))
print(b,id(b))
s()
