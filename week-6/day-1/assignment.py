# Assignment – Week 6 – Day 1
# Q1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Ask n from user.
n= int(input(" enter your number: "))
dic={}
for i in range(1,n+1):
    dic[i]=i*i
print(dic)
# Q2. Write a Python program to check if a dictionary is empty or not.
a={}
b={
    "name":"tirth"
}
print(len(a)>0)
print(len(b)>0)
# Q3. Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
c={}
for i in d1:
    if i in d1 and i in d2:
        c[i]=d1[i]+d2[i]
    else:
        c[i]=d1[i]

for i in d2:
    if i not in d1:
        c[i]=d2[i]
print(c)
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# Q4. Python program to find the size of a Dictionary. Basically print how many total key-value pair are there.
a={}
b={
    "name":"tirth"
}
print(len(a))
print(len(b))
# Q5. Write a Python program to remove duplicates from Dictionary.
# Sample dictionary: dictionary = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7:60, 8:50}
# Output: {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10}

