alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
"x", "y", "z"
]

# for letter in alphabet:
#     print(letter)

# rand_num = (int)(input("Pick a number between 1 and 25.."))

def rand_letter():
    print(alphabet[rand_num])
rand_letter()

def letter_num():
    user_num=input("Please enter a number between 1 and 26:     >")
    user_num=int(user_num)
    user_num -=1
    if user_num >=0 and user_num <=26:
        print(alphabet[user_num])
    else:
        print("Invalid entry please try again")
        letter_num()
    
letter_num()
