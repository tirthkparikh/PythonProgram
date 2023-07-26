"""
Ask 3 marks from user. Out of 100

If pass in all subjects
Then only print total and percentage

FAIL
"""

maths = int(input("enter maths matks out of 100:  "))
phy = int(input("enter phy matks out of 100: "))
chem = int(input("enter chem matks out of 100: "))


if 0<maths<100 and 0<phy<100 and 0<chem<100:
   if maths>33 and chem>33 and phy>33:
       print(f"passed with total {maths+phy+chem}/100 and {(maths+phy+chem)*100/300}" )
else:
    print("enter proper marks")