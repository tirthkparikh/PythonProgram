# Q1. Make your own list of numbers. Ask a start and end position from User. Print the list from start position to end position using Slicing.

a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
start = int((input("Enter start pos: ")))
end = int((input("Enter end pos: ")))
print(a[start:end])



# Q2. Make your own list of numbers. Ask a start and end position from User. Make another different list which will contain number from start to end position. Use slicing logic.

a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
start = int((input("Enter start pos: ")))
end = int((input("Enter end pos: ")))

if start<end:
    b=a[start:end]
else:
    b=a[start:end:-1]

print(b)


# Q3. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list. Using slicing logic.

a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
num=int(input("end value :  "))
print(a[-num:])


# Q4. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list but in reverse order. Using slicing logic.

a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
num=int(input("end value :  "))
print(a[-1:-num-1:-1])





# For Q5, the program will interchange the first and last elements in the list and print the original list and the interchanged list.
a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 7]
a[0],a[-1]=a[-1],a[0]
print(a)
# For Q6, the program will split the list into two halves using list slicing and print both halves. Note that if the list has an odd number of elements, the first half will have one less element than the second half.
a=[54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
mid = len(a) // 2
print("First half:", a[:mid])
print("Second half:", a[mid:])





