# Q1. Write a Python program to get the 4th element from the last element of a tuple.
a=(1,2,3,4,5,6,7,8,9,0)
print(a[-4])


# Q2. Write a Python program to find repeated items in a tuple.
a=(1,2,7,4,7,6,7,8,9,0)
b=[]
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
    if i not in b:
        b.append(i)
   

print(c)

    
# Q3. Write a Python program to check whether an element exists within a tuple.
a=(1,2,7,4,7,6,7,8,9,0)
num=int(input("to check value"))
print(a.count(num)>0)
# Q4. Write a Python program to remove an item from a tuple.
# we cannot change tupple we can make a new tupple
a=(1,2,3,4,5,6,7,8,9,0)
b=list(a)
del b[0]
c=tuple (b)
print(c)

# Q5. Write a Python program to reverse a tuple.
# we cannot change tupple we can make a new tupple
a=(1,2,3,4,5,6,7,8,9,0)
b=list(a)
c=b[::-1]
d=tuple(c)
print(d)


# Q6. Write a Python program to check if a string has at least one letter and one number. If it has at least one letter and one number then print YES else print NO.

a="tirth12"
alpha=False
num=False
for i in a:
    if i.isalpha():
        alpha=True
    if i.isnumeric():
        num=True
if alpha and num:
    print("yes")
else:
    print("no")
# Q7. Write a python program to ask a string from user. Then count the number of vowels and number of consonants in that string.

value =input("enter value: ").lower()

count=0
count2=0
for i in value:
    if i=="a" or i=="e" or i=="i" or i=="o"  or i=="u":
        count+=1
    elif i.isalpha():
        count2+=1
        
print("vowels are", count)
print("constant are", count2)


# Q8. Ask a string from user. Print the string with first 2 letters and last 2 letters.
# Example string: aeroplane
# Output: aene
a="aeroplane"
print(a[:2]+a[-2:])

# Q9. Write a python program to only print the second half of the string. Ask string from user.
# Example string: aeroplane
# Output: lane
# Example string: delhi
# Output: hi

a="delhi"
half = len(a) // 2
second_half = a[half+1:]
print("Output:", second_half)