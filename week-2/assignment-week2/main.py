#1
unit = int(input("Enter the number of units: "))
rate = float(input("Enter the rate per unit: "))

total_cost = unit*rate + unit*rate*0.12

if total_cost > 100 and total_cost % 5 == 0:
        print(f"The cost of your light bill is Rs{total_cost}. There is a free gift card to your favorite store")

else:
        print(f"The cost of your light bill is Rs{total_cost}")


#2

units = int(input("Enter total units used: "))

if units <= 50:
        total_unit_bill = units * 0.50
elif units <= 150:
        total_unit_bill  = 50 * 0.50 + (units - 50) * 0.75
elif units <= 250:
        total_unit_bill  = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
else:
        total_unit_bill  = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50


total = total_unit_bill*0.20 + total_unit_bill

print(f"Total Electricity Bill is Rs{total}")




angle1 = float(input("Enter the 1st angle for your triangle: "))
angle2 = float(input("Enter the 2nd angle for your triangle: "))
angle3 = float(input("Enter the 3rd angle for your triangle: "))


if angle1+angle2+angle3 == 180:

    if angle1 == angle2 == angle3:
        print("The triangle is equilateral.")
        #equilatrel triangle can never be right-agnled as they all will have 60
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("The triangle is isosceles.")
        #isosceles traingle can be equilatrol
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("The triangle is right-angled.")
    else:
        print("The triangle is scalene.")
        #scalene traingle can be equilatrol
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("The triangle is right-angled.")

else:

    print("enter proper angles")


number = int(input("Enter an integer: "))
value = abs(number)
print(f"Absolute value for {number} is {value}.")





char = input("Enter a character: ").lower()

if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("it is a vowel.")
else:
    print("it is a consonant.")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


largest= num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")