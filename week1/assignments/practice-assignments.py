"""
Q1. Write a program to check if a given character is a vowel or a
consonant.
"""
character = str(input("Enter a character: ")).lower()

if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")


"""
Q2. Write a program to check if a given number is even or odd.
"""

number = int(input("Enter your number here:  "))

if number%2 ==0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")


"""
Q3. Write a program to check if a given number is a multiple of 3
and 5.
"""

checkMultiple = int(input("Enter your number here to check multiple:  "))

if checkMultiple%3 ==0 and checkMultiple%5==0:
      print(f"{checkMultiple} is multiple of 3 and 5 ")
elif checkMultiple%3 ==0:
     print(f"{checkMultiple} is multiple of 3 and not 5 ")
elif checkMultiple%5 ==0:
     print(f"{checkMultiple} is multiple of 5 and not 3 ")
else:
     print(f"{checkMultiple} is not amultiple of 5 or 3 ")
     
"""
Q4. Write a program to compare two numbers and print the larger
number.
"""
num_1= int(input("Enter your 1st number here:  "))
num_2=  int(input("Enter your 2nd number here:  "))
if num_1>num_2:
     print(f"{num_1} is the greater value than {num_2}")
else:
     print(f"{num_2} is the greater value than {num_1}")


"""
Q5. Write a program to find the absolute value of a given number.
"""
num = int(input("Enter your  number here:  "))
print(f"{abs(num)} is absolute value of {num}")

"""
Q6. Write a program to determine the greatest among three given
numbers.
"""
number_1 =int(input("Enter your 1st number here:  "))
number_2 =int(input("Enter your 2nd number here:  "))
number_3 =int(input("Enter your 3rd number here:  "))

if number_1>number_2 and number_1>number_3:
     print(f"{number_1} is greatest of three")
elif number_1<number_2 and number_2>number_3:
     print(f"{number_2} is greatest of three")
else:
     print(f"{number_3} is greatest of all 3")


"""
Q7. Write a program to calculate the total cost of a hotel stay
based on the number of nights and the room rate per night. Apply
a 10% tax to the total cost.
"""
roomCost = int(input("Enter total cost of room per night: "))
hotelDays = int(input("Enter total days of your stay: "))

totalRoomCost = roomCost*hotelDays
totalCost = totalRoomCost+ totalRoomCost*0.1
print(f"Total cost of hotel stay with 10% tax is: f{totalCost} ")

"""
Q8. A group of friends decided to participate in a cooking
competition. In the first round, each friend had to prepare a dish,
and the judges scored each dish on a scale of 1 to 10. The scores
for the friends&#39; dishes are as follows:
Friend 1: 7
Friend 2: 9
Friend 3: 6
Friend 4: 8
Friend 5: 7
Now, based on these scores, calculate the following?
 The highest score among the friends.
 The lowest score among the friends.
 The average score of all the friends&#39; dishes.

"""
friend1_score = 7
friend2_score = 9
friend3_score = 6
friend4_score = 8
friend5_score = 7


highest_score = friend1_score
if friend2_score > highest_score:
    highest_score = friend2_score
if friend3_score > highest_score:
    highest_score = friend3_score
if friend4_score > highest_score:
    highest_score = friend4_score
if friend5_score > highest_score:
    highest_score = friend5_score


lowest_score = friend1_score
if friend2_score < lowest_score:
    lowest_score = friend2_score
if friend3_score < lowest_score:
    lowest_score = friend3_score
if friend4_score < lowest_score:
    lowest_score = friend4_score
if friend5_score < lowest_score:
    lowest_score = friend5_score


average_score = (friend1_score + friend2_score + friend3_score + friend4_score + friend5_score) / 5

print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Average Score:", average_score)

"""
Q9. A school is organizing a field trip, and the students are divided
into buses based on the number of students in each class. The
number of students in each class is as follows:
Class 1: 25 students
Class 2: 32 students
Class 3: 28 students
Class 4: 30 students

Class 5: 27 students
Now, based on these class sizes, answer the following questions?
 What is the total number of students in all the classes
combined?
 How many buses are needed if each bus can accommodate
a maximum of 35 students?
 How many students will be left over after filling the buses with
the maximum capacity?
"""
class1_students = 25
class2_students = 32
class3_students = 28
class4_students = 30
class5_students = 27


total_students = class1_students + class2_students + class3_students + class4_students + class5_students


bus_capacity = 35

if total_students % bus_capacity != 0:
    extra_bus = 1
else:
    extra_bus =0
buses_needed = total_students // bus_capacity + extra_bus

students_left_over = total_students % bus_capacity

print("Total number of students:", total_students)
print("Number of buses needed:", buses_needed)
print("Number of students left over:", students_left_over)