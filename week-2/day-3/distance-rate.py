"""
Distance Rate Calculator 

Ask distance from user (km)

Base Price upto 5km - 100Rs
5-10km -> 50rs/km
10-15km -> 40rs/km
15-20km -> 30rs/km
20 above -> 15rs/km

3km -> 100Rs

7km -> 5+2 -> 100+100 -> 200
10km -> 5+5 -> 100+250 -> 350
13km -> 5+5+3 -> 100+250+120 -> 470
18km -> 5+5+5+3 -> 100+250+200+90 -> 640
23km -> 5+5+5+5+3 -> 100+250+200+150+45 -> 745
43km -> 5+5+5+5+23 -> 100+250+200+150+(15*23) -> 1045

"""

distance=int(input("enter the distance in km:  "))

if distance<0:
    print("invalid")
elif 0<distance<=5:
    print(100)
elif 5<distance<=10:
        print(100+(distance-5)*50)
elif 10<distance<=15:
        print(100+250+(distance-10)*40)
elif 15<distance<=20:
        print(100+250+200+(distance-15)*30)
elif distance>20:
    print(100+250+200+150+((distance-20)*15))