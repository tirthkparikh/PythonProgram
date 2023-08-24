# a = [54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]

# num =int(input("Enter the number: "))

# b=[]
# for i in range(len(a)):
#     if a[i]==num:
#         b.append(i)

# if len(b):
#     for i in b:
#         print(f"num is located at {i}")
# else:
#     print("num not present")

a = [54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45,2,1,1,1,54,54,676]

num = int(input("Enter the number: "))

positions = []
for i in range(len(a)):
    if a[i] == num:
        positions.append(i)

if positions:
    print(f"The number exists at positions: {positions}")
else:
    print("Number does not exist.")

