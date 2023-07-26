# question dosenot specify int or float so taken int in input
num_1 = int(input("Enter first number for summation: "))
num_2 = int(input("Enter second number for summation: "))
print(f"summation of {num_1} + {num_2} = {num_1+num_2}")


# question dosenot specify int or float so taken float in input
kilometers = float(input("Enter the distance in kilometers: "))
print(f"{kilometers} kilometers is equal to {kilometers*0.621371} miles.")


# question dosenot specify int or float so taken int in input and float in output
avg_1 = int(input("Enter first number for average : "))
avg_2 = int(input("Enter second number for average: "))
avg_3 = int(input("Enter third number for average: "))
print(f"average of {avg_1},{avg_2} and {avg_3} is {float((avg_1+avg_2+avg_3)/3)}")



rupees = float(input("Enter value in rupees=  ")) 
print(f"{rupees} rupees is {rupees*100} paise")

# question dosenot specify int or float so taken float in input
length = float(input("Enter the side length of the square: "))
print(f"The area of the square with side length {length} is {length**2}.")



gamesPlayed = int(input("Enter the number of games played: "))
gamesWon = int(input("Enter the number of games won: "))
gamesLost = int(input("Enter the number of games lost: "))

gamesTied = gamesPlayed - gamesWon - gamesLost

totalPoints = (gamesWon*4) + (gamesTied*2)

print("Number of ties:", gamesTied)
print("Total points:", totalPoints)