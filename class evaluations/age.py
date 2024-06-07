# Write a script to handle users age and print their category
# 0 - 2 = infant
# 3 - 11 = kids
# 12 - 19 = teenager
# 20 - 34 = young adult
# 35 - 69 = adult
# 70 - 99 = old man

print("welcome")
age = input("kindly enter your age ")
age = int(age)
if 0 <= age <= 2:
    print("infant")
elif 3 <= age <= 11:
    print("kids")
elif 12 <= age <= 19:
    print("teenager")
elif 20 <= age <= 34:
    print("young adult")
elif 35<= age <= 69:
    print("adult")
elif 70<= age <= 99:
    print("oldman")
else:
    print("thank you")