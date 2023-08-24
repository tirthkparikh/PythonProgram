details = {
    "Anirudh": {
        "age": 55,
        "city": "Surat",
        "phone": 5678567,
        "marks": [11, 22, 33, 44, 55],
    },
    "Sagar": {
        "age": 11,
        "city": "Delhi",
        "phone": 985474587,
        "marks": [65, 12, 76, 88, 33],
    },
    "Muskan": {
        "age": 16,
        "city": "Agra",
        "phone": 8585747474,
        "marks": [98, 21, 54, 73, 88],
    },
}


# for k,v in details.items():
#     total=0
#     for i,z in v.items():
#         if i == "marks":
#             for c in z:
#                 total+=c
#     print(total)
#     v["total"]=total
    
# print(details)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone=int(input("enter your number: "))
marks=list(map(int,input("enter marks: ").split()))
details[name]={"age":age, "phone":phone,"marks":marks    
        }
print(details)
    



