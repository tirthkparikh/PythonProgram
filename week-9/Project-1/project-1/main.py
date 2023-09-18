# Project 1
# Quiz Application

# Objective:
# Develop a quiz application that asks the user multiple-choice questions and
# tracks their score. Utilize Python basics such as lists, loops, and conditional
# statements to create the application.

# Requirements:
# 1. Use lists to store questions, answer choices, and the correct answers.
# 2. Use loops to iterate through the questions.
# 3. Use conditional statements to determine if the user&#39;s answer is correct.
# 4. Display the user&#39;s score at the end of the quiz.
# 5. (Optional) Provide feedback based on the user&#39;s performance.

# Instructions:
# 1. Create a list of questions and their corresponding answer choices. You
# may include at least 5 questions to start with.
# 2. For each question, create a list of possible answer choices, with one
# correct answer.
# 3. Implement a loop to display each question and its answer choices to
# the user.
# 4. Allow the user to input their answer choice and use a conditional
# statement to determine if it&#39;s correct.

# 5. Keep track of the user&#39;s score throughout the quiz.
# 6. After the user has answered all the questions, display their final score.
# 7. (Optional) Provide feedback based on the user&#39;s score, such as &quot;Great
# job!&quot; for high scores or &quot;Keep practicing!&quot; for low scores.



name=input("Enter your name to start the game: ")
print()
print(f"Welcome {name}")
print()
TotalPoints=50
yourScore=0
ListOfQuesionsOprtionsAns=[
    {
        "question": "Which team has won the most IPL titles as of 2021?",
        "options": ["a) Chennai Super Kings", "b) Mumbai Indians", "c) Kolkata Knight Riders", "d) Royal Challengers Bangalore"],
        "correct_answer": "b"
    },
    {
        "question": "Who holds the record for the most runs scored in a single IPL season?",
        "options": ["a) Chris Gayle", "b) Virat Kohli", "c) David Warner", "d) AB de Villiers"],
        "correct_answer": "a"
    },
    {
        "question": "Which IPL team is known as the 'Orange Army'?",
        "options": ["a) Rajasthan Royals", "b) Kings XI Punjab", "c) Sunrisers Hyderabad", "d) Delhi Capitals"],
        "correct_answer": "c"
    },
    {
        "question": "Who is the highest wicket-taker in the history of IPL as of 2021?",
        "options": ["a) Jasprit Bumrah", "b) Lasith Malinga", "c) Amit Mishra", "d) Dwayne Bravo"],
        "correct_answer": "b"
    },
    {
        "question": "Which city's team does Shikhar Dhawan represent in the IPL?",
        "options": ["a) Delhi", "b) Kolkata", "c) Mumbai", "d) Chennai"],
        "correct_answer": "a"
    }
]
flag=False
for item in ListOfQuesionsOprtionsAns:
    for k,v in item.items():
        if k == "question":
            print(f"Q.{v}")
        if k== "options":
            for i in v:
                print(i,end=" ")   
        if k=="correct_answer":
            print()
            user_ans=input("Enter Your choice(a,b,c,d):  ").lower()
            if user_ans[0] in "abcd":
                if user_ans[0]==v:
                    print("you have entered right answer")
                    print()
                    yourScore+=10
                else:
                    print("uh-oh wrong answer focus more")
                    print()
            else:
                flag=True
                print("Enter proper answer/ Game restart")
                break
    if flag:
        break
if not flag:
    print("Your score is ",yourScore)
    if yourScore>40:
        print("you are Real champion")
    elif yourScore>=30:
        print("nice Work")
    else:
        print("Work Harder")

    



