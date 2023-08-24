"""
key-value pair
key always uniqe
"""

a={
    "name":"Tirth",
    "age":22,
    "gender":"Male"
}
print(a)
print(type(a))
print(a["name"])
print(a.get("name"))
print(a.items())
print(a.keys())
print(a.values())
print(a.copy())
a["married"]="no"
print(a)
# name={a}
# print(name)
name,age,gender,married=a.values()
print(name)
