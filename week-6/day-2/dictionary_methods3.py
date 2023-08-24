a = {"m1": 67, "m2": 98, "m3": 78, "m4": 31, "m5": 67, "m6": 62, "m7": 67}

print(a["m3"])
print(a.get("m3"))

key = input("Enter yor key = ")

result = a.get(key)

# if result == None:
#     print("Key not found")
# else:
#     print(result)

if key not in a:
    print("not found")
else:
    print(a[key])
