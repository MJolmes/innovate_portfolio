alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
"x", "y", "z"
]

for i in alphabet:
    print(i)


rand_num = (int)(input("Pick a number between 1 and 25.."))

def rand_letter():
    print(alphabet[rand_num])
rand_letter()
