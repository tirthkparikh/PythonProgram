# i=1
# count=0
# while i<=20:
#     if i%3==0:
#         count+=1
#     i+=1
# print(count)





start_2 = int(input("Enter the start number: "))
end_2 = int(input("Enter the end number: "))


total = 0
while start_2  <= end:
    if start_2  % 4 == 0:
        total += start_2 
    start_2  += 1

print("Sum of numbers divisible by 4=", total)