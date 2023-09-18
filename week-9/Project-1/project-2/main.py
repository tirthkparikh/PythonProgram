password = input("Enter your password: ")

lengthCriteriaMet = False
uppercaseCriteriaMet = False
lowercaseCriteriaMet = False
numberCriteriaMet = False
specialCharCriteriaMet = False

if len(password) >= 8:
    lengthCriteriaMet = True

for char in password:
    if char.isupper():
        uppercaseCriteriaMet = True
        break

for char in password:
    if char.islower():
        lowercaseCriteriaMet = True
        break

for char in password:
    if char.isdigit():
        numberCriteriaMet = True
        break

specialCharacters = "!@#$%^&*"
for char in password:
    if char in specialCharacters:
        specialCharCriteriaMet = True
        break

criteriaMetCount = sum([lengthCriteriaMet, uppercaseCriteriaMet, lowercaseCriteriaMet, numberCriteriaMet, specialCharCriteriaMet])

if criteriaMetCount >=4:
    strength = "Strong"
elif criteriaMetCount >= 3:
    strength = "Moderate"
else:
    strength = "Weak"

print(f"Password Strength: {strength}")
