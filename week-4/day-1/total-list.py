a = [23, 54, 65, 32, 23, 54, 65, 7]

# total=0
# for i in a:
#     total+=i
# print(total)
# print(sum(a))
# print(max(a))

total=0
for i in a:
    if i%2==0:
        total+=i
print(total)

