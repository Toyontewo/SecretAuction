# Nesting Dictionary in a Dictionary

# games_log = {
#     "Football": {"good_at": ["Fifa 14", "Fifa 13", "Fifa 18", "Fifa 21", "Fifa 22"]},
#     "total_visits": 35,
#     "Adventure": ["Harry Potter", "Call of duty", "Rainbow Vegas"],
# }
# print(games_log["total_visits"])

# Nesting a Dictionary in a list
travel_log = [
    {
        "country": "France",
        "good_at": ["Fifa 14", "Fifa 13", "Fifa 18", "Fifa 21", "Fifa 22"],
        "total_visits": 35
    },
    {
        "country": ['Harry Potter', "Call of duty", "Rainbow Vegas"],
        "total_visits": 5
    },

]


def add_new_country(counrty_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = counrty_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
add_new_country("Nigeria", 3, ["Ibadan", "Lagos", "Abuja", "Calabar"])
print(travel_log)
