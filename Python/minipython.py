# Variables + Basics
#
#first_name = "Mr."
#last_name = "Bean"
#full_name = first_name +" "+ last_name
#print("Hello "+full_name)
#print(type(name)

# Variables
#age = 17
#age += 1
#print("Your age is: "+str(age))
#print(type(age))

# Floating points
#height = 250.5
#print("Your height is: "+str(height)+"cm")
#print(type(height))

# Booleans
#human = True
#print("Are you a human: "+str(human))
#print(type(human))

# Multiple Assignment

#name = "Sean"
#age = 17
#attractive = True

#name, age, attractive = "Sean", 17, True

#print(name)
#print(age)
#print(attractive)

#Spongebob = Patrick = Sandy = Squidward = 30
#print(Spongebob)

#name = "Sean"

#print(len(name))
#print(name.find("S"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("e"))
#print(name.replace("e","a"))
#print(name*2)

# Type Casting
# Variables
#x = 1 #int
#y = 2.0 #float
#z = "3" #str No maths on strings!

#x = str(x)
#y = str(y)
#z = str(z)

#print("X is "+str(*x))
#print(y)
#print(z*3)

# User Input
#name = input("What is your name?: ")
#age = int(input("How old are you?:"))
#height = float(input("How tall are you?: "))

#age = age + 1

#print("Hello "+name)
#print("You are "+str(age)+" years old")
#print("You are "+str(height)+"cm tall")

# Imported Math library for advanced mathematical functions
#import math

#pi = -3.14
# x = 1
# y = 2
# z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(420))
#print(max(x,y,z)) --> Maximal value of all variables
#print(min(x,y,z)) --> Minimal value

# String Slicing

#name = "John Doe"

#first_name = name[:3]
#last_name = name [4:]
#funky_name = name[::2]
#reversed_name = name[::-1]

#print(reversed_name)

# Silicing Strings

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"
#slice = slice(7,-4)

#print(website1[slice])
#print(website2[slice])

# Various Statements

#age = int(input("How old are you?: "))

#if age == 100:
    #print("You are a century old!")
#elif age >= 18:
    #print("You are an adult!")
#elif age < 0:
    #print("You haven't been born yet!")
#else:
    #print("You are a child!")

# Logical Operators

#temp = int(input("What is the temperature outside? "))

#if not(temp >=0 and temp <= 30):
    #print("The temperature is bad today")
    #print("Stay inside!")
#elif not(temp < 0 or temp > 30):
    #print("The temperature is good today!")
    #print("Go outside!")

# While loops

#name = None

#while not name:
    #name = input("Enter your name: ")

#print("Hello "+name)

# For loops will be executed a limited amount of times

#for i in range(50,101,2):
    #print(i)

#for i in "John Doe":
    #print(i)

#import time 

#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Happy new year!")

# Nested Loops

#rows = int(input("How many rows?"))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end="")
    #print()

# Loop Control Statements

#while True:
    #name = input("Enter your name: ")
    #if name != "":
        #break

#phone_number = "123-456-7890"

#for i in phone_number: 
    #if i == "-":
        #continue
    #print(i, end="")

#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i)

# Lists

#food = ["pizza","hamburger","spaghetti","sushi"]

#food[0] = "Borgir"

#print(food[0])

#food.append("ice cream")
#food.remove("sushi")
#food.pop()
#food.insert(0,"cake")
#food.sort()
#food.clear()

#for x in food:
    #print(x)

# 2D Lists

#drinks = ["coffee","soda","tea"]
#dinner = ["pizza","hamburger","hotdog"]
#dessert = ["cake","ice cream"]

#food = [drinks,dinner,dessert]

#print(food[1][2])

# Tuples

#student = ("Sean",21,"male")

#print(student.count("Sean"))
#print(student.index("male"))

#for x in student:
    #print(x)

#if "Sean" in student:
    #print("Hello Sean!")


# Sets

#utensils = {"hammer","knife","fork","spoon","spoon","spoon"}
#dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)

#print(utensils.difference(dishes)) # Roles can be reversed!
#print(utensils.intersection(dishes))

#for x in dinner_table:
    #print(x)


# Dictionary

#capitals = {'USA':'Washington DC',
             #'India':'New Dehli', 
             #'China':'Beijing',
             #'Russia':'Moscow'}

#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'Las Vegas'})
#capitals.pop('China')
#capitals.clear()

#print(capitals['Germany'])
#print(capitals.get('Germany')) #Safer Way!
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for key,value in capitals.items():
    #print(key, value)


# Index Operator

#name = "john doe!"

#if(name[0].islower()):
    #name = name.capitalize()

#first_name = name[:4].upper()
#last_name = name[4:].lower()
#last_character = name[-1]

#print(first_name)
#print(last_name)
#print(last_character)

# Functions

#def hello():
    #print("hello! "+name)
    #print("Have a nice day!")

#hello("Sean")


