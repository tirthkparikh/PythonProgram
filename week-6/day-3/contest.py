# WEEK 6 - Contest (5 questions)
# Q1. Create a dictionary that counts the frequency of words in a given string. Ask string from user.

# Example 1
# Input String: "The sun is shining and the weather is nice"

# Output:
# {
#     'The': 1,
#     'sun': 1,
#     'is': 2,
#     'shining': 1,
#     'and': 1,
#     'the': 1,
#     'weather': 1,
#     'nice': 1
# }

# Example 2
# Input String: “The cat and the dog played in the park The cat chased the dog”

# Output:
# {
#     'The': 2,
#     'cat': 2,
#     'and': 1,
#     'dog': 2,
#     'played': 1,
#     'in': 1,
#     'the': 3,
#     'park': 1,
#     'chased': 1
# }

arr = input("enter your string").split()

b={}
for i in arr:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
# Q2. Combine two dictionaries into a single dictionary, adding values for common keys.

# Dictionary 1
# {
#     'a': 10,
#     'b': 20,
#     'c': 30
# }

# Dictionary 2
# {
#     'b': 5,
#     'c': 15,
#     'd': 25
# }

# Output Dictionary
# {
#     'a': 10,
#     'b': 25,  # Value added: 20 + 5
#     'c': 45,  # Value added: 30 + 15
#     'd': 25
# }

a={'a': 10,
   'b': 20,
  'c': 30}
b={
       'b': 5,
    'c': 15,
    'd': 25 
}

c={}
for i in a :
    if i in a and i in b:
       c[i]=a[i]+b[i]
    else:
        c[i]=a[i]

for i in b:
    if i not in c:
        c[i] =b[i]

print(c)
# Q3. Write a Python program to map two lists into a dictionary. Everything in both lists should be unique.

# Example 1
# list1 = ['red', 'green', 'blue']
# list2 = ['#FF0000','#008000', '#0000FF']

# Output: {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

# Example 2
# a = [“Anirudh”, ”Sanjay”, ”Sagar”]
# b = [33, 66, 88]

# Output: {“Anirudh”:33, ”Sanjay”:66, “Sagar”:88}


a = ["tirth","sonali","keyur"]
b = [33, 66, 88]
c={}
for i in range(len(a)):
    print(a[i])
    c.update({a[i]:b[i]})
    # c[a[i]]=b[i]
print(c)







# Q4. Write a Python program to convert string values of a given dictionary into integer/float data types.

# Example 1:
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

# Output:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

# Example 2:
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

# Output:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
a=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

print(f"Orignal array:{a}")
for i in a:
    for k,v in i.items():
        i[k]=float(v)

print(f"changed array:{a}")




# Q5. Write a Python program to convert a dictionary into a list of lists. (HARD)

# Example 1
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

# Result:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

# Example 2
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

# Result:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

b=list(a.keys())
c=list(a.values())
d=[]
f=[]
for i in range(len(b)):
    d.append([b[i],c[i]])
print(d)
for k,v in a.items():
    f.append([k,v])
print(f)
