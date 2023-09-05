students = [
    {
        "name": "Anirudh",
        "marks": 89,
    },
    {
        "name": "Sagar",
        "marks": 11,
    },
    {
        "name": "Sanjay",
        "marks": 6,
    },
    {
        "name": "tirth",
        "marks": 156,
    },
]

def highestMarks(students):
    max1=0
    for i in students:
        if i["marks"]>max1:
            max1=i["marks"]
            student=i["name"]
    return(max1,student)
print(highestMarks(students))
        