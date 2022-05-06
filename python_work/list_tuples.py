list1 = [
    1,2,3
]

tuple1 = (
    1,2,3
)

# coffee_order = [
#     "will - americano",
#     "katy - cappucino"
# ]
# print(coffee_order[0])
# # change order
# coffee_order[0] = "will - americano"

# print(coffee_order[0])
# # print through the orders in the object
# for i in coffee_order:
#     print(i)

# coffee_tuple = (
#     "nick - mocha",
#     "marcus - black"
# )

# for i in coffee_tuple:
#     print(i)

# # update nicks order
# coffee_tuple[0] = "Nick - Decaf mocha"

# for i in coffee_tuple:
#     print(i)


#------------------------

# choose an item in a list, in another list
# list_of_lists = [
#     [1, 2, 3], #1
#     [4, 5, 6]  #0
# ]

# print(list_of_lists[1][0]) # this will print 4


#---------------------- Tuples + Lists
# Lists can be altered, Tuples remain constant

# even_nums = [2, 4, 6, 8, 10] # [] Square brackets means List

# odd_nums = (1, 3, 5, 7, 9) # () Brackets means a Tuple

# even_nums.append(12) # Adds 12 to end
# even_nums.insert(3, 0) # (place in the list (3), the number added to list(0))

# for i in even_nums:
#     print(i)

# odd_nums.pop()  # Won't work as it can't change a 'Tuple'


# -----------------Lists Start & Stop 
# list_of_fruit = [
#     "apples",
#     "oranges",
#     "bananas",
#     "pears",
#     "mango",
#     "cherries"
# ]

# print(list_of_fruit[1:-1])
# print(list_of_fruit[0:6])
# print(list_of_fruit[1:])

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(nums[0:11:3]) # Start, stop & step [0:11:3]

# num = 0

# while num <10:
#     print(num)
#     num += 1

#---------------- While Loop --------------

some_vari = "some input from user"

list_of_fruit = [
    "apples",
    "oranges",
    "bananas",
    "pears",
    "mango",
    "cherries"
]
while some_vari:
    print("The user has spoken")
    if "oranges" in list_of_fruit:
        print("Vitamin C!")
        break
    else:
        print("Add oranges")
        fruit = input()
        list_of_fruit.append(fruit)
        continue




