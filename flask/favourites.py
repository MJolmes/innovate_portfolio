music_list = [
    {
        "artist":"DigablePlanets",
        "artist":"DigablePlanets2"
    },
    {
        "artist":"DigablePlanets3",
        "artist":"DigablePlanets4"
    },
    {
        "artist":"DigablePlanets5",
        "artist":"DigablePlanets6"
    }
]

fave_bands = ["abcd"]


for dict_i in music_list:
    fave_bands.append(list(dict_i.values())[0])
    print(list(dict_i.values())[0])
    # print(dict_i)
    # print(dict_i.values())

def add_to_list(band):
    fave_bands.append(band)

def del_from_list(band):
    fave_bands.remove(band)




