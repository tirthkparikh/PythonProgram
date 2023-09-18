# # Q1. Calculate the sum of all numbers in a text file:
with open("file.txt", "r") as file:
    total = 0
    value=file.readlines()
    print(value)
    for i in value:
        total+=int(i)
    print(total)        
        

# # Q2. Check if a word exists in a file:

word= input("Enter a word : ").lower()
flag=False
with open("tex.txt", "r") as file:
    value=file.readlines()
    for i in value:
        for letter in i.split() :
            if letter.lower() == word:
                flag=True
if flag:
    print("Yes")
else:
    print("NO")

# Q3. Ask a word from user. Count the frequency of how many times that number comes in a file.

word= input("Enter a word : ").lower()
coun=0
with open("tex.txt", "r") as file:
    value=file.readlines()
    print(value)
    for i in value:
         for j in i.split():
             if j==word:
                 coun+=1
    print(coun)


# Q4. Print words in reverse order:
with open("reverse.txt", "r") as file:
    for line in file:
        words = line.split()
        reverse= " ".join(word[::-1] for word in words)
        print(reverse)




 
# Q5. Write a python program. Only print those lines which contains ‘a’ in it.
with open("reverse.txt", "r") as file:
     for line in file:
        if 'a' in line:
            print(line.strip())