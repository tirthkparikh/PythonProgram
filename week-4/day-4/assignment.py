# 1. Write code that takes a list of numbers as input and calculates the sum of all the elements in the list. Remember first take input, and then calculate the sum without using sum() function.

num=int(input("Enter total number you want to add: "))
a=[]
for i in range(num):
    value=int(input(f"enter number {i+1}: "))
    a.append(value)
total=0
for i in a:
    total+=i
print(total)

# 2. Write code that takes a list as input, removes all duplicate elements from it.
num=int(input("Enter total number you want to add: "))
a=[]
for i in range(num):
    value=int(input(f"enter number {i+1}: "))
    a.append(value)
b=[]

for i in a:
 if b.count(i)==0:
    b.append(i)
print(b)

# 3. Write code that takes two lists and prints the elements that are common to both lists.
num=int(input("Enter total number you want to add in list 1: "))
num1=int(input("Enter total number you want to add in list 2: "))
a=[]
b=[]
for i in range(num):
    value=int(input(f"enter number {i+1} for list 1: "))
    a.append(value)
for i in range(num1):
    value=int(input(f"enter number {i+1} for list 2: "))
    b.append(value)
for i in a:
   for j in b:
      if i==j:
         print(i,end=" ")
print()

# 4.  Write code that takes a list of numbers as input and prints a new list with the squares of each element.
num=int(input("Enter total number you want to add: "))
a=[]
for i in range(num):
    value=int(input(f"enter number {i+1}: "))
    a.append(value)

for i in a:
    print(i*i,end=" ")
print()
# 5. Write code that checks if a given list is a palindrome, i.e., it reads the same backward as forward. Print "Palindrome" if it is, otherwise print "Not a Palindrome".
val=int(input("Enter total number you want to add: "))
a=[]
flag=True
for i in range(val):
    chr=input(f"enter {i+1} elemnt for list: ")
    a.append(chr)
for i in range(len(a)):
    if a[i]!=a[len(a)-1-i]:
        flag=False

if flag:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 6. Write code that takes a list of elements as input and prints the count of each unique element along with the element itself.

num=int(input("Enter total number you want to add in list 1: "))
a=[]
b=[]
c=[]
for i in range(num):
    value=int(input(f"enter number {i+1}: "))
    a.append(value)
for i in a:
 if b.count(i)==0:
    b.append(i)
    c.append(a.count(i))

for i in range(len(b)):
   print(f"element:{b[i]} its count is {c[i]}")



# 7. Write code that takes a list of numbers and an integer 'n' as input. Print the index of the first occurrence of 'n' in the list, or print "Not found" if 'n' is not present.
n=int(input("Enter number you wish to find: "))
num=int(input("Enter total number you want to add: "))
a=[]
for i in range(num):
    value=int(input(f"enter number {i}: "))
    a.append(value)

x=a.index(n)   
print(x)



# 8. Write code that takes a list of numbers as input and calculates the sum of elements at even indices and the sum of elements at odd indices separately. Print both sums.

num=int(input("Enter total number you want to add: "))
a=[]
for i in range(num):
    value=int(input(f"enter number {i}: "))
    a.append(value)

totalEven=0
totalOdd=0
for i in range(len(a)):
    if i%2==0:
      totalEven+=a[i]
    else:
       totalOdd+=a[i]
print(f"total of even index = {totalEven}")
print(f"total of odd index = {totalOdd}")