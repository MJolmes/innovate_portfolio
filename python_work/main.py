# import person as pn
from person import Person

# liam = pn.Person("Liam", 30, "6'7''")
liam = Person("Liam", 30, "6'7''")
katy = Person("Katy", 30, "5'2''")
demi = Person("Demi", 30, "5'8''")

liam.set_hair("Brown, curly hair")
katy.set_hair("Long, black hair")
demi.set_hair("Long, ginger")

liam.talk()

