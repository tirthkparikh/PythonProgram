# Q1. Write a Python program to check if a string is empty or not.
a=""
b="a"

if len(a):
    print("not empty")
else:
    print("empty")
if len(b):
    print("not empty")
else:
    print("empty")


# Q2. Write a Python program to find the length of the longest word in a string.


b=list(input("enter your string").split())

largest=0
for i in b:
    if len(i)>largest:
        largest=len(i)

print(largest)


# Q3. Write a Python program to find the most common character in a string. (Print the letter which repeats most of the time)
a=input("enter your string = ")
b = [item for item in a]
largest=0
value=0
for i in b:
     if b.count(i)>largest:
         largest=b.count(i)
         value=i

print(value,largest)


# Q4. Write a Python program to remove duplicate characters from a string and return the modified string.
a=input("enter your string = ")
b = [item for item in a]
c=[]

for i in b:
    if i not in c:
        c.append(i)

a="".join(item for item in c)
print(a)