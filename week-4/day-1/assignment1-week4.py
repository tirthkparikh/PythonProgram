

# Q1. Make a list. Print the length of that list.
a=[56,43,21,58,99,113]
print(len(a))


# Q2. Make a list. Tell if the length of that list is Even or Odd.
b=[56,43,21,58,99,113]
if len(a)%2==0:
    print("Even")
else:
    print("odd")



# Q3. Make a list. Find the sum of all the elements in list which are
# divisible by 3.
total=0
c=[12,3,5,8,9]
for i in c:
    if i%3==0:
        total+=i
print(total)


# Q4. Make a list. Find how many positive and negative numbers are
# there.
d=[-12,3,-5,8,-1,23,5,8,9]
posCount=0
negCount=0
for i in d:
    if i>0:
        posCount+=1
    else:
        negCount+=1
print(f"positive Count={posCount}, negative count={negCount}")


# Q5. Make a list. Print all the elements in a list in reverse order.
e=[-12,3,-5,8,-1,23,5,8,9]
for i in range(len(e)-1,0,-1):
    print(e[i],end=" ")
print()

# Q6. Make a list. Now print all the elements based on even
# index/position
# Example:
# my_list=[45, 12, 59, 60, 47, 3412, 3111]
# Output:
# 45 59 47 3111
my_list=[45, 12, 59, 60, 47, 3412, 3111]
for i in range(0,len(my_list),2):
    print(my_list[i],end=" ")
