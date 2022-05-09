class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age

    def talk(self):
        print(f"Hello my name is {self.name}, I am {self.age} years old, and {self.height} tall.")
    
    def set_hair(self, hair):
        self.hair = hair
        # print(self.hair)
        print(f"{self.name} has {self.hair} hair")





will = Person("Will", 31, "6'0''")
marcus = Person("Marcus", 32, "5'10''")

# will.talk()
# marcus.talk()






