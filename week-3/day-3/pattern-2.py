"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
n=int(input("enter the num: "))
for i in range (0,n):
    for j in range(1,n+1):
        print(j, end=" ")
    print()