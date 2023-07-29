"""
1st

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


2nd

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 

3rd


* * * * *
*       *
*       *
*       *
* * * * *


4rd

Ask a start number = 
Ask a end number = 

Print all prime numbers between them.
"""



#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# for i in range(0,5):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for j in range(0,2*i+1):
#         print("*",end=" ")
#     print()


#         * 
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         * 


# for i in range(0,5):
#     for j in range(i,6):
#         print(" ",end=" ")
#     for j in range(0,2*i+1):
#         print("*",end=" ")
#     print()

# for i in range(5,-1,-1):
#     for j in range(5,i-1,-1):
#      print(" ",end=" ")
#     for j in range(2*i+1,0,-1):
#         print("*",end=" ")
#     print()


# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# n=int(input("enter your num"))

# for i in range(0,n):
#     if i==0 or i==n-1:
#      for j in range(0,n):
#         print("*",end=" ")
#      print()
#     else:
#      print("*",end=" ")
#      for j in range(1,n-1):
#         print(" ",end=" ")
#      print("*",end=" ")
#      print()


# n=int(input("enter your num: "))
# z=int(input("enter your num: "))

# for i in range(n,z):
#     x=True
#     for j in range(2,int(n**(1/2)+2)):
#         if i%j==0:
#             x=False
#             break
            
#     if x:
#         print(f"{i} ")