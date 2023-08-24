details={
    "tirth":{
        "age":24,
        "city":"ahmedebad",
        "marks":[50,65,85,70,80]
    },
    "keyur":{
        "age":45,
        "city":"patdi",
        "marks":[50,65,85,70,80]
    },
    "sonali":{
        "marks":[50,65,85,70,80],
        "city":"Bavla"
    }
}
print(details["tirth"].keys())

# for k,v in details.items():
#     age=v["age"]
#     print(f"age of {k} is {age}")

for k, v in details.items():
    print(f"Name = {k}")
    if v.get('age'):
        print(f"Age = {v['age']}")
    print(f"City = {v['city']}\n")
    
details = {
    "Anirudh": {
        "age": 55,
        "city": "Surat",
        "phone": 5678567,
        "marks": [11, 22, 33, 44, 55],
    },
    "Sagar": {
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


for k, v in details.items():
    total=0
    for i in v['marks']:
        total+=i
    print(f"total marks of {k} is {total}")

for k, v in details.items():
    print(f"total marks of {k} is {sum(v['marks'])}")