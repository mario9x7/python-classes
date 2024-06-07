# write a script to evaluate students performance based on their grades
# 0 - 39 fail 
# 40 - 44 poor
# 45 - 49 fair
# 50 -59 good
# 60 - 69 very good
# 70 - 100 excellent

print("welcome")
grades = input("kindly enter your grades  ") 
grades = int(grades)
if 0 <= grades <= 39:
    print("fail")
elif 40 <= grades <= 44:
    print("poor")
elif 45 <= grades <= 49:
    print("fair")
elif 50 <= grades <= 59:
    print("good")
elif 60 <= grades <= 69:
    print("very good")
elif 70 <= grades <= 100:
    print("excellent")
else: 
    print("please input a valid score") 