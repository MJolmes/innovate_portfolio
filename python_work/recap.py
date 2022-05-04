import random

# strings are for representing characters
print("hello there")
print("1234")

# This is an integer - a whole number
print(1234)

# This is a floating point - anything with a decimal
print(1234.5) 

# Booleans - True or False
print(True)
print(False)

# None - a blank, or null type
print(None)

# Len - counts number of characters in a string
print(len("hello"))

# Index Position ------------

# Prints "e" - first character is 0
print("hello"[1])
# Prints "o" - the last character
print("hello"[-1])

# .notation is a way of accessing methods
print("hello".upper())

# Libraries ----------------

print(random.random())
print(random.uniform(1,10))  # A random decimal(floating point) from 1 to 10
print(random.randint(1,10))  # A random whole number(integer) from 1 to 10

import random
from random import random,randint,uniform


my_name = "Marcus"
my_age = 32

print("Hello my name is",my_name)
print("Hello I am " + my_name) # Has to be string with string - no numbers
print("Hello my name is {} and I am {} years old".format(my_name,my_age)) # Using {} can mix string and numbers
print(f"Hello my name is {my_name} is and I am {my_age}") # Most readable and easy to edit

print(1+2)
print(2-1)
print(2*3)
print(3**3)
print(15/3)
print(15%3)

balance = 100
amount = 50

print(balance-amount)
balance = balance - amount
balance -=amount
print(balance)

# Inputs ---------

# char_name = input("What is your name?   >  ")

# print(f"Welcome, {char_name}")

# IF statement ------  == means equal to. != means not equal to
music = "classical"

if music == "classical":
    print("Oh no it's classical")
elif music == "pop":
    print("Turn it up")
else:
    print("Yay")

num1=10
num2=20

if num1 > num2:
    print("Number one is the bigger number")
elif num1<num2:
    print("number 2 is the bigger number")
else:
    print("number 1 and number 2 are the same")

num = 14

if num%7==0 and num%3==0:
    print("fizzbuzz")
elif num%3==0:
    print("fizz")
elif num%7==0:
    print("buzz")
else:
    print(num)

place = "Manchester"
weather = "Cloudy"

if place=="Manchester" and weather=="Rainy":
    print("Of course")
elif place=="Manchester" and weather=="Sunny":
    print("Check again")
else:
    print("It's bloody windy")

day="Saturday"
bank_holiday=True

if day=="Saturday" or day=="Sunday" or bank_holiday==True:
    print("It's a day off!")
else:
    print("Time to go to Code Nation")

# FUNCTIONS --------------------------------------

def light_switch():
    print("Who turned the lights out?!")

light_switch()
light_switch()

def cash_withdrawal(amount, accnum):
    print(f"Withdrawing {amount} from account {accnum}")

cash_withdrawal(300,12345678)

def add_up(num1,num2):
    return num1+num2

print(add_up(5,2))

# LISTS ------------------------------------

fav_films = [
    "Jurassic Park",
    "Lost World",
    "Jurassic Park"
]
print(fav_films[0]) #Prints 1st item in list

fav_films[2]="Spiderman" #Changes 3rd item in list
print(fav_films)

fav_films.append("Spiderboy") #Adds to list
print(fav_films)

fav_films.pop() #Remove last item, or what is put in parametres e.g. .pop(1)
print(fav_films)

# i INDEX --------------------

for i in fav_films:
    print("That's a great film")

# for i in range(10):
#     print(i)
#OR
for i in range(3,12,2): # Goes from start '3' to end '12', the 2 makes it stop 2 places before 12
    print(i)

num=0

while num <10:
    num +=1
    print(num)
