#Capitalize method 
name= "mario"
#converts the first character to uppercase
print(name.capitalize())

#Casefold method
school= "LINAR"
#converts string into lowercase
print(school.casefold())

#center method
fruit= "banana"
x=fruit.center(50)
print(x) 

#count method
fruit=["orange", "pineapple", "apple" , "pineapple", "pineapple"]
x= fruit.count("pineapple")
print(x)

#istrip method
car= "BMW"
x= car.lstrip()
print("of all cars", x, "is my favorite car")

'''

do= input("what do you do\n")
suffix= input("Enter your suffix\n")
suffixstrip= suffix.lstrip()
print(f"You are a {do + suffixstrip}")
'''

#join method
name_of_student = ("Hb", "grace", "great")
x= ", ".join(name_of_student)
print(f'Names of Student are {x}')

#lower method
intro= "HELLO EVERYONE, WELCOME TO LINAR"
x= intro.lower()
print(x)

#maketrans method
intro= "hello cain! can you cry"
x= str.maketrans("c","p")
print(intro.translate(x))

local = "All payment should be in $"
x= str.maketrans("$","N")
print(local.translate(x))

#partition method
text= "i could run codes all day"
x=text.partition("codes")
print(x)

#replace method
text= "I like going to the club"
x= text.replace("club", "class")
print(x)

#rjust method
text= "linar"
x=text.rjust(10)
print(x, "is my favorite school")

#split method
introduction= "welcome to linar academy"
x= introduction.split()
print(x)

#strip method
institute= "linar"
x= institute.strip()
print("of all school",x,"is my favorite of them all")

#zfill method
number= "100"
x= number.zfill(20)
print(x)