dict_of_cat = {
    "Name" : "Striper",
    "Colour" : "Black and gold",
    "Breed" : "Calico",
    "Fav Food" : "Tuna",
    "Current State" : "Napping",
    "Days since last incident" : 4
}

dict_of_cat["Fav Food"] = "Dreamies"
dict_of_cat["Current State"] = "Slinkin' about"
dict_of_cat["Days since last incident"] = 0

dict_of_cat.update({"Top_speed" : 900})

# # for i in dict_of_cat.values():    ???????
# #     if i == "Striper":
# #         i = "None"

# print(dict_of_cat)

countries = {
    "United Kingdom" : "London",
    "France" : "Paris",
    "Germany" : "Berlin",
    "Spain" : "Madrid",
    "Italy" : "Rome"
}

countries.setdefault("Mother Russia", "Moscow")

print(countries)