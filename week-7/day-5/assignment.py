# Week 7 - Dictionary Questions (9 questions)

# Q1. Make a dictionary on your own, with mixed key values. (Key can be any data type and value can be any data type). Then ask a value (K) from the user. Remove all the keys from the dictionary having values greater than K.

# Example 1
# test_dict = {"Anirudh":"Male","xyz":8,"Sagar":"1111","Pqr":2,"ABBC":9}
# K = 6
# Output = {'Anirudh': 'Male', 'Sagar': '1111', 'Pqr': 2}

# Example 2
# test_dict = {"Anirudh":"Male","xyz":-8,"Sagar":"1111","Pqr":2,"ABBC":9}
# K = 1
# Output = {'Anirudh': 'Male', 'xyz': -8, 'Sagar': '1111'}


test_dict = {"Anirudh":"Male","xyz":8,"Sagar":"1111","Pqr":2,"ABBC":9}
arr=[]
k=int(input("Hello enter number: "))
for j,v in test_dict.items():
 if type(v) == int  and v > k:
        arr.append(j)
for i in arr:
    test_dict.pop(i)
print(test_dict)


# Q2. Write a Python program to convert more than one list to a nested dictionary.

# Example 1
# student_id = ["S001", "S002", "S003", "S004"] 
# student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
# student_grade = [85, 98, 89, 92]

# Output = [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

# Example 2
# student_id = [1, 2, 3, 4]
# student_name = ["Anirudh", "Sagar", "Sanjay", "Vandana"]
# student_grade = [55, 89, 51, 13]

# Output = [{1: {'Anirudh': 55}}, {2: {'Sagar': 89}}, {3: {'Sanjay': 51}}, {4: {'Vandana': 13}}]

student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
obj={}
for i in range(len(student_id)):
    obj[student_id[i]]={student_name[i]:student_grade[i]}

print(obj)

# Q3. Write a Python program to filter the height and weight of students, which are stored in a dictionary. Ask height and weight from the user. Make your own dictionary.

# Example 1
# students = {
#     "Alice Smith": (6.3, 72),
#     "Bob Johnson": (5.9, 68),
#     "Eva Brown": (6.1, 74),
#     "Jake Davis": (6.0, 70),
# }
# height = 6.0
# weight = 70

# Output = {'Alice Smith': (6.3, 72), 'Eva Brown': (6.1, 74), 'Jake Davis': (6.0, 70)}

# Example 2
# students = {
#     "Liam Wilson": (6.2, 75),
#     "Olivia Martinez": (5.8, 68),
#     "Noah Anderson": (6.4, 80),
#     "Emma Garcia": (5.9, 71),
# }
# height = 5.5
# weight = 78

# Output = {'Noah Anderson': (6.4, 80)}

students = {
    "Liam Wilson": (6.2, 75),
    "Olivia Martinez": (5.8, 68),
    "Noah Anderson": (6.4, 80),
    "Emma Garcia": (5.9, 71),
}
h = 5.5
w = 78
arr=[]
for k,v in students.items():
    if v[0]<h or v[1]<w:
        arr.append(k)
for i in arr:
    students.pop(i)
print(students)
# Q4. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. Make list on your own.

# Example 1
# colors = [("green", 1), ("purple", 2), ("orange", 3), ("green", 4), ("blue", 1)]
# Output = {'green': [1, 4], 'purple': [2], 'orange': [3], 'blue': [1]}



# Example 2
# colors = [("cyan", 1), ("magenta", 2), ("cyan", 3), ("yellow", 4), ("magenta", 1)]
# Output = {'cyan': [1, 3], 'magenta': [2, 1], 'yellow': [4]}

# Example 3
# colors = [
#     ("red", 1),
#     ("blue", 2),
#     ("green", 3),
#     ("red", 4),
#     ("blue", 1),
#     ("green", 2),
#     ("red", 3),
#     ("blue", 4),
#     ("green", 1),
# ]
# Output = {'red': [1, 4, 3], 'blue': [2, 1, 4], 'green': [3, 2, 1]}

colors = [
    ("red", 1),
    ("blue", 2),
    ("green", 3),
    ("red", 4),
    ("blue", 1),
    ("green", 2),
    ("red", 3),
    ("blue", 4),
    ("green", 1),
]
obj={}
for k,v in colors:
    if k in obj:
            obj[k].append(v)
    else:
            obj[k] = [v]

# Q5. Make your own dictionary, sort the dictionary by values.

# Example 1
# data = {"apple": 5, "banana": 2, "orange": 8, "grape": 1}
# Output = {'grape': 1, 'banana': 2, 'apple': 5, 'orange': 8}

# Example 2
# data = {"English": 5, "Maths": 2, "Science": 14}
# Output = {'Maths': 2, 'English': 5, 'Science': 14}

data = {"apple": 5, "banana": 2, "orange": 8, "grape": 1}
data_list = list(data.items())

# Sort the list based on values
data_list.sort(key=lambda item: item[1])

# Convert the sorted list back to a dictionary
sorted_data = dict(data_list)

print(sorted_data)

# Q6. Write a Python program to convert a dictionary into a list of lists.

# Example 1
# data = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# output = [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

# Example 2
# data = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# output = [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
data = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
output = []
for key, value in data.items():
        output.append([key, value])
print(output)
# Q7. Write a Python program to filter even numbers from a dictionary of values.

# Example 1
# data = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# output = {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}

# Example 2
# data = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# output = {'V': [], 'VI': [], 'VII': [2]}
data = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
output = {}
for key, values in data.items():
        evenValues = [value for value in values if value % 2 == 0]
        output[key] = evenValues
print(output)
# Q8. Write a Python program to find the shortest list of values for the keys in a given dictionary.

# Example 1
# data = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
# output = ['VI', 'VIII', 'X']

# Example 2
data = {
    "A": [5, 10, 15],
    "B": [20, 25],
    "C": [30, 35, 40],
    "D": [45],
    "E": [50, 55, 60],
    "F": [65, 70],
    "G": [75, 80, 85],
    "H": [90],
    "I": [95, 100],
}

# output = ['D', 'H']


min_length = float('inf')
shortest_keys = []
    
for key, values in data.items():
    if len(values) < min_length:
            min_length = len(values)
            shortest_keys = [key]
    elif len(values) == min_length:
            shortest_keys.append(key)

print(shortest_keys)

# Q9. Write a Python program to count the frequency of a dictionary.

# Example 1
# dictt = {
#     "V": 10,
#     "VI": 10,
#     "VII": 40,
#     "VIII": 20,
#     "IX": 70,
#     "X": 80,
#     "XI": 40,
#     "XII": 20,
# }
# output = {10: 2, 40: 2, 20: 2, 70: 1, 80: 1}

# Example 2
dictt = {
    "A": 10,
    "B": 20,
    "C": 30,
    "A": 10,
    "D": 40,
    "E": 20,
    "F": 30,
    "G": 40,
}
# output = {20: 2, 30: 2, 40: 2, 10: 1}

frequency = {}
for value in dictt.values():
    if value in frequency:
            frequency[value] += 1
    else:
            frequency[value] = 1
print(frequency)