# Q1. Reverse the order of words in a sentence. For example, change "Hello World" to "World Hello".

# Example 1:
# Input: "Hello World"
# Output: "World Hello"

# Example 2:
# Input: "Coding is fun"
# Output: "fun is Coding"

# Example 3:
# Input: "Python programming"
# Output: "programming Python"


a="Hello world"
ch=a.split()
print((" ").join(item for item in ch[-1::-1]))


# Q2. Given a list of strings, concatenate them into a single string separated by spaces. For example, given the input ["Hello", "World", "Python"], the output should be "Hello World Python".

# Make a list on your own.
# Don’t use the JOIN function.
a=["Hello", "World", "Python"]
str=""
for i in a:
    
    str+=i
    if i is not "Python":
     str+=" "
     
str+="."
print(str)


# Q3. Write a program to rotate the characters in a string by a given number of positions. For example, given the input "abcdef" and rotation of 2, the output should be "efabcd".

# Ask string and rotation from the user.
a="abcdef"
b="defabc"
i=-1
print(a[-i::]+a[:-i:])


# Q4. Given two strings s1 and s2. The task is to find out the minimum number of string rotations for the given string s1 to obtain the actual string s2.

# Example 1
# Input:
# s1 = "abcd"
# s2 = "cdab"

# Output:
# 2

# Example 2
# Input:
# s1 = "hello"
# s2 = "lohel"

# Output:
# 2

# Example 3
# Input:
# s1 = "programming"
# s2 = "mingprogram"

# Output:
# 4

# Example 4
# Input:
# s1 = "abcdef"
# s2 = "defabc"


str="abcdef"
str1="defabc"

 


for i in range(len(str)):
    str = str[-1]+str[:-1]
    if str==str1:
        print(i+1)


# Q5. Write a Python program to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

# Input: pyTHon
# Output: PYTHON

# Input: helLo
# Output: helLo

# Input: gOOD
# Output: GOOD


str="pytHon"
new=[char for char in str[:4:1]]
count=0
for i in new:
    if i.isupper():
        count+=1

if count>=2:
    print(str.upper())

