fav_songs = [
    {
        "artist" : "Digable Planets", "song_name" : "Good to be here",  "Genre" : "Hiphop",  "release_year" : "1994"
    },
    {
        "artist" : "The Outfit", "song_name" : "Rise & Shine",  "Genre" : "Hiphop",  "release_year" : "1995"
    },
    {
        "artist" : "Los Lobos", "song_name" : "Live and Let Live",  "Genre" : "Hiphop",  "release_year" : "1993"
    },
    {
        "artist" : "Wu-Tang Clan", "song_name" : "Hellz Wind Staff",  "Genre" : "Hiphop",  "release_year" : "1996"
    }
]

fav_songs.append({"artist" : "Loyle Carner", "song_name" : "Angel",  "Genre" : "??",  "release_year" : "2017"})
fav_songs.pop(-2)

fav_songs[0] = {"artist" : "Dig", "song_name" : "Good",  "Genre" : "Hip",  "release_year" : "1990"}
# fav_songs.update({"Top_speed" : 900})
# fav_songs[0[0]] = {"artist" : "PIE"}


for each_dict in fav_songs:
    print("\n")
    for dict_value in each_dict.values():
        print(dict_value)
