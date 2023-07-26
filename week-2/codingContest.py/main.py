#1
#a
i=10
while i<=200:
    print(i,end=" ")
    i+=10


#b
print("\n")
j=1
while j<=100000000:
    
    print( j,end=" ")
    j=j*10



#c
print("\n")
k=1
while k<=1111111111:
    
    print( k,end=" ")
    k=k*10+1

#d
j=1
start = 1
end = 28

print("\n")

while start <= end:
     if j == 1:
         print(start, end=" ")
         start+=2
     elif j%2 == 0:
         print(start, end=" ")
         start+=3
         
     else:
         print(start, end=" ")
         start+=2
     j+=1 

#e
print("\n")
s=1
e=2048
while s<=e:
    print(s,end=" ")
    s*=2

#########################################################
#2
print("\n")
n = int(input("Enter a value: "))
sum=1
inc = 1
while inc<=n:
    sum += 1 / (2 ** inc)
    inc += 1

print(sum)

######################

#3
print("\n")
start_1=1
end_1=10
sum_2=0
while start_1<=end_1:
    sum_2 = start_1**2 + sum_2
    start_1+=1
print(sum_2)
   

###########################

#4
print("\n")
st=1
while st<=100:
    if st % 2 == 0 and st % 3 == 0 and st % 8 != 0:
        print(st,end=" ")
    st+=1
