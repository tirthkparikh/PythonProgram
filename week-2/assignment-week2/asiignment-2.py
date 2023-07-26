#1

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))


while start <= end:
    print(start)
    start += 1


#2

start_1 = int(input("Enter the start number: "))
end_1 = int(input("Enter the end number: "))


while start_1 <= end_1:
    if start_1 % 5 == 0 or start_1 % 7 == 0:
        print(start_1)
    start_1 += 1



#3


start_2 = int(input("Enter the start number: "))
end_2 = int(input("Enter the end number: "))


total = 0
while start_2  <= end_2:
    if start_2  % 4 == 0:
        total += start_2 
    start_2  += 1

print("Sum of numbers divisible by 4=", total)



#4
i=1
product=1
while i<=10:
    product=product*i
    i+=1

print(product)


#5
number = int(input("Enter a number: "))
j=1
while j<=10:
    total=j*number
    print(f"{number} X {j} = {total}")
    j+=1


#6
k=20
count=0
while k<=70:
    if k%4 ==0:
        count+=1
    k+=1
print(count)


#7


number_1 = int(input("Enter a number: "))
k=2
flag=0

while i<=int(number_1**0.5)+1:
     if number_1 % k == 0:
            flag=1
            break
     k+=1

if flag==1:
    print("not prime")
else:
    print("prime")
     





