a = {
    "name": "Anirudh Khurana",
    "age": 33,
    "gender": "Male",
    "m1": 55,
    "m2": 99,
    "m3": 88,
}
print(list(a.items()))
print(list(a.values()))
print(list(a.keys()))
# for k in a.keys():
#     print(f"{k} - {a[k]}")

# for v in a.values():
#     print(v)

# for item in a.items():


for k, v in a.items():
    print(k, v)
