marks = float(input("enter your makes: "))

if 0<=marks<=100:
    if 90<marks<=100:
        print("you got Grade A")
    elif 80<marks<=90:
        print("you got Grade B")
    elif 70<marks<=80:
        print("you got Grade c")
    elif 60<marks<=70:
        print("you got Grade D")
    else:
        print("you got Grade E")
else:
    print("invalid")