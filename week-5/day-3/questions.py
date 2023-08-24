# value =input("to check palindrome: ").lower()
# flag=True
# p1=0
# p2=len(value)-1
# while p1<p2:
#     if value[p1]!=value[p2]:
#         flag=False
#         break
#     p1+=1
#     p2-=1
# if flag:
#     print("Palindrome")
# else:
#     print("not a Palindorme")



# value =input("enter value: ").lower()

# count=0
# for i in value:
#     if i=="o":
#         count+=1

# print("count of o is",count)       


# value =input("enter value: ").lower()

# count=0
# for i in value:
#     if i=="a" or i=="e" or i=="i" or i=="o"  or i=="u":
#         count+=1
# print("vowels are", count)


value =input("enter value: ")

if value.isnumeric():
    print(2*int(value))
else:
    print("not a num")