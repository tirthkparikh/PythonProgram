# LIST COMPREHENSION QUESTIONS

# Write a list comprehension to square each element in a given list.
# Input: [1, 2, 3, 4]
# Output: [1, 4, 9, 16]

input= [1, 2, 3, 4]
print([item**2 for item in input])


# Create a list comprehension to filter out odd numbers from a given list.
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 4, 6, 8, 10]
input= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([item for item in input if item%2==0])

# Generate a list comprehension to extract all vowels from a given string.
# Input: "hello world"
# Output: ['e', 'o', 'o']
input="hEllo world"
print([item for item in input if item.lower() in "aeiou"])

# Calculate the length of each word in a sentence using list comprehension.
# Input: "This is a sample sentence"
# Output: [4, 2, 1, 6, 8]
input= "This is a sample sentence"
print([len(item) for item in input.split() ])

# Reverse each word in a list of strings using list comprehension.
# Input: ["hello", "world", "python"]
# Output: ['olleh', 'dlrow', 'nohtyp']
input=["hello", "world", "python"]
print([item[::-1] for item in input])
# Count the frequency of each character in a string using list comprehension.
# Input: "hello"
# Output: [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
input = "hello"
output=[]
x={}
[output.append((char, input.count(char))) for char in input if char not in [item[0] for item in output]]
print(output)



# Write a list comprehension to remove duplicates from a given list.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

input = [1, 2, 2, 3, 4, 4, 5]
output=[]
[output.append(item) for item in input if item not in output]
print(output)

# Create a list of individual characters from a given string.
# Input: "hello"
# Output: ['h', 'e', 'l', 'l', 'o']
input= "hello world"
print([item for item in input if item !=" "])

# Generate a list of squares of numbers at odd indices from a given list.
# Input: [1, 2, 3, 4, 5, 6]
# Output: [4, 16, 36]
input= [1, 4, 3, 4, 5, 6, 7, 8, 9, 10]
print([input[item]**2 for item in range(len(input)) if item%2!=0])

# Find the intersection of two lists using list comprehension.
# Input: [1, 2, 3, 4], [3, 4, 5, 6]
# Output: [3, 4]
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print([item for item in list1 if item in list2])

# Create a dictionary mapping each character in a string to 'vowel' if it's a vowel, and 'consonant' if it's a consonant.
# Input: "hello"
# Output: {'h': 'consonant', 'e': 'vowel', 'l': 'consonant', 'o': 'vowel'}
input_string = "hello"
vowels = "aeiou"  # List of vowels
output = {char:"vowel" if char.lower() in vowels else 'consonant' for char in input_string}
print(output)
