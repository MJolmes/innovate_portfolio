

def enter_num():
    num = int(input("Please enter a number! >  "))

    while num ==True:
        print(f"You entered {num}, that is a {type(num)} input")
        break
    else:
        print("Try again")
        enter_num() 
        



enter_num() 