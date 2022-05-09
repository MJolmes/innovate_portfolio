def enter_num():
    num = int(input("Please enter a number! >  "))

    if num -+0:
        print(f"You entered {num}, that is a {type(num)} input")
    else:
        print("Try again")
        enter_num() 
        
enter_num() 

# def num_check():         # a function called num_check - it doesn't take any parameters in this case
#     num=input("Please type in a number")      # take an input from the user
# ​
#     try:     # the program will attempt to do this line WITHOUT any fatal errors
#         num=int(num) # casting - changing the data type to an int, because input is always a string
#         print(f"The number you picked is {num} and it is a {type(num)}") #type prints the type of the data - this was asked for in the brief!
#     except:  # if a fatal error does occur - this will happen instead
#         print("This is not an integer - try again") # try again message
#         num_check()   # self-recursive to give the user the chance to try again
# ​
# num_check() #calling the function