"""
loops in python
to repeat process
1.while
2.for
"""

"""
1 to 100

Divisible 6 -> Total
"""
# total=0
# i=1
# while i<=100:
#     if i%6 == 0:
#         total+=i
#     i+=1
# print(total)


# num = int(input("enter start number: "))
# num2 = int(input("enter end number: "))
# num3 = int(input("enter any number: "))

# while num<=num2:
#     if num%num3 == 0:
#        print(num)
#     num+=1


user_number = int(input("Enter a number: "))
i=2
flag=0
while i<=int(user_number**0.5)+1:
     if user_number % i == 0:
            flag=1
            break
     i+=1
     
if flag==1:
    print("not prime")
else:
    print("prime")
     


