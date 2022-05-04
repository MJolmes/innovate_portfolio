alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
"x", "y", "z"
]

for i in alphabet:
    print(i)


response = int(input("Please choose from 1 to 26: "))
if response < 27:
    print("yes")
    # alphabet == nums
    # print(f"{nums[input]}")
