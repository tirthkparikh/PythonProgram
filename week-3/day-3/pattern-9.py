"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

"""
if we see that number is decresing in loop from 5 t0 1 in run
we can think of reversing row 
"""
