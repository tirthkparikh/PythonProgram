# Q1. Write a Python program to check a list is empty or not.
a = [54, 1, 43, 234, 7, 7, 87]
b=[]

if len(a)>0:
    print("List not empty")
else:
    print("empty")

if len(b)>0:
    print("List not empty")
else:
    print("empty")


# Q3. Write a Python program to find the second smallest number in
# a list.

# considiring sorting not allowed
a = [54, 1, 43, 234, 1, 3, 87]

# taking high values initally as dont know how to get infinite value
smallest=100000000
second_smallest=9999999
for i in range(0,len(a)):
    if a[i]<smallest:
        second_smallest=smallest
        smallest=a[i]
    else:
        if a[i]<second_smallest and a[i]!=smallest:
            second_smallest =a[i]
print(second_smallest)




# Q4. Write a Python program to find the second largest number in a
# list.


# considiring sorting not allowed


# taking low values initally as dont know how to get infinite value

a = [54, 1, 43, 234, 1, 3, 87,87,234]
largest= -100000
second_largest= -1111111

for i in range(0,len(a)):
    if a[i]>largest:
        second_largest=largest  
        largest=a[i]
    else:
        if a[i]>second_largest and a[i]!=largest:
            second_largest =a[i]

print(second_largest)



# Q6. Take 10 integer inputs from user and store them in a list. Now,
# copy all the elements in another list but in reverse order.

c=[]
d=[]
for _ in range(10):
     num = int(input(f" Enter the {_+1} number for list:  "))
     c.append(num)

c.reverse()
d=c
# # we can also append c to d in loop and then reverse  it will resolve issue of pass by refrence

print(d)

# Q7. Write a program to find the average of all the numbers present
# in the list.
a = [54, 1, 43, 234, 1, 3, 87,87,234]
total=0
for i in a:
    total+=i
print(f"avg value is {total/len(a)}")


# Q8. Make 2 different list. First merge both list into third variable. And
# sort the merge list in descending order.

b = [100, 211, 113, 4, 76, 73, 13]
a = [54, 1, 43, 234, 1, 3, 87,87,234]
c=[]
for i in a:
    c.append(i)
for i in b:
    c.append(i)
c.sort(reverse=True)
print(c)

# Q9. Make a list. Write a simple program for addition of the 2 nd
# element from start and 2 nd element from the end.

d=[]
for _ in range(10):
     num = int(input(f" Enter the {_+1} number for list:  "))
     d.append(num)

    
print(f"total is {d[1]+d[-2]}",d)