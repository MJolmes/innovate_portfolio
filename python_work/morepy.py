# print (int(5.9))   # int will round down the number to 5
# print (int(round(5.9)))     # (int'(round))' will round up
# print (int("54"))   # Turns string into an integer

# print (float(54))   # Makes into floating point

# print (str(5.4))    # Turns into string

# print (type(str(5.4)))  # '(type)' shows type of data


#-------------------- Truth & Falsy --------------

# print("what is your name?")
# name = input()
# if name:
#     print(f"Hello {name}")
# else:
#     print("You did not provide a name")


# print(not True)    # 'not True' swaps to False
# print(not False)    # 'not False' swaps to True

# bool = False
# if bool != True:
#     print(False)
# else:
#     print(True)

#     # OR #

# bool = True
# if not bool:
#     print(False)
# else:
#     print(True)


#------------- Adding 2 numbers from inputs -----------------

# def add_up():
#     num1 = input("First no. to add? \n")
#     num2 = input("Second no. to add? \n")
#     print(int(num1) + int(num2))
# add_up()

    # OR #

# def add_up():
#     num1 = input("First no. to add? \n")
#     num2 = input("Second no. to add? \n")
    
#     try:
#         print(f"{num1} + {num2} is {int(num1) + int(num2)}")
#     except:
#         print("Error")
#         print("************")
#         add_up()  
# add_up()


#----------- Light Switch ------------

# light = False

# def light_switch():
#     global light
#     if light:
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True

# light_switch()
# light_switch()


#------------- Bank Account -----------------

# balance = 100

# def cash_withdraw(amount):
#     global balance
#     print(f"Your balance is {balance}")
#     print(f"You are withdrawing {amount}")
#     balance-=amount
#     print(f"Your balance is {balance}")

# cash_withdraw(int(input("amount")))
# cash_withdraw(20)
# cash_withdraw(20)








