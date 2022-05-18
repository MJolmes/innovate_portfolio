countries = {
    "United Kingdom" : "London",
    "France" : "Paris",
    "Germany" : "Berlin",
    "Spain" : "Madrid",
    "Italy" : "Rome"
}

countries.setdefault("Russia", "Moscow")
countries.setdefault("Portugal", "Lisbon")

print(countries)

for i, value in countries.items(): # This method is good for readability but could take up a lot of space.
    print(i, ' : ', value)

countries["United Kingdom"] = "English"
countries["France"] = "French"
countries["Germany"] = "German"
countries["Spain"] = "Spanish"
countries["Italy"] = "Italian"
countries["Russia"] = "Russian"
countries["Portugal"] = "Portugese"

for i, value in countries.items(): 
    print(i, ' : ', value)
