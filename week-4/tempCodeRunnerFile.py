# Make your own list, find the largest element from that list without using the sort() method.
# num=int(input("Enter total number you want to add: "))
# a=[]
# for i in range(num):
#     value=int(input(f"enter number {i+1}: "))
#     a.append(value)

# print(max(a))


# # Q2. Make your own list. Ask a frequency from the user. Print only those numbers in that list which have count greater than or equal to the frequency entered by the user.

# a = [54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45,2,1,1,1,54,54,676,1]


# freq= int(input("enter frequency: "))

# b=[]
# for i in a:
#     if i not in b:
#         if a.count(i)>=freq:
#             b.append(i)

# for i in b:
#     print(i,end=" ")
# print()

# # Make your own list, calculate the product of all the numbers excluding the duplicates.

# num=int(input("Enter total number you want to add: "))
# a=[]
# for i in range(num):
#     value=int(input(f"enter number {i+1}: "))
#     a.append(value)

# b=[]
# for i in a:
#     if a.count(i)<2:
#         b.append(i)

# if len(b):
#     product = 1
#     for i in b:
#         product*=i
#     print(product)
# else:
#     print(0)


# # . Find the missing number from the list, the numbers missing from the list should only be printed. Make sure the list you take is always sorted.
# list1 =[1,4,5,7,20]
# # if list is not sorted sort it
# missing=[]

# # len(list1)
# print(len(list1))
# for i in range(list1[0],list1[len(list1)-1]):
#      if i  not in list1:
#          missing.append(i)
# print(missing)