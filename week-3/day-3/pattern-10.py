"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5

*
* *
* * *
* * * *
* * * * *

1
2 3 
4 5 6
7 8 9 10
11 12 13 14 15

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

1 2 3 4 5
2 3 4 5
3 4 5
4 5
5

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

Enter n = 8
8
7 8
6 7 8
5 6 7 8
4 5 6 7 8
...
1 2 3 4 5 6 7 8
"""


# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()



# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()


# 1
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# k=1
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(k,end=" ")
#         k+=1
#     print()


# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# for i in range (0,5):
#     for j in range (5,i,-1):
#         print(j,end=" ")
#     print()



# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

# for i in range (0,5):
#     for j in range (i+1,6):
#         print(j,end=" ")
#     print()


# Enter n = 8
# 8
# 7 8
# 6 7 8
# 5 6 7 8
# 4 5 6 7 8
# ...
# 1 2 3 4 5 6 7 8


# n=int(input("enter the number: "))
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(j,end=" ")
#     print()
    

