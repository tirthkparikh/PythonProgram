"""
Ask a string from user. 
Ask a character from user.
Ask new character from user.

Replace character with new character from
the string entered by user.

hello
o
z

hellz
"""

value =input("enter value: ")
old_char = input("old char: ")
new_char = input("new char: ")
print(value.replace(old_char,new_char))