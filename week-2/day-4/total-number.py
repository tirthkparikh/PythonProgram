"""
total from 1 to 10
"""
# i=1
# total=0
# while i<=10:
#     total+=i
#     i+=1
# print(total)


start = int(input("enter start number: "))
end = int(input("enter end number: "))
total =0
while start<=end:
    total+=start
    start+=1
print(total)