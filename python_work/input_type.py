# def enter_num():
#     num = int(input("Please enter a number! >  "))

#     if num -+0:
#         print(f"You entered {num}, that is a {type(num)} input")
#     else:
#         print("Try again")
#         enter_num() 
        
# enter_num() 

def enter_num():       
    num=input("Please type in a number   ")     
    try:     
        num=int(num)   
        print(f"The number you picked is {num} and it is a {type(num)}") 
    except:
        print(f"You entered {num} and that is a {type(num)}")

enter_num() 