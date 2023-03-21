from enum import IntEnum


class Cuisine(IntEnum):
    Italian = 1.
    Polish = 2.
    Japanese = 3.


class Name(IntEnum):
    Id1 = 1.
    Id2 = 1.
    Id3 = 3.
    Id4 = 4.


# there should be a class Dish, each of dish must have same features, also when it is set to zero
database = [
    {"name": Name.Id1, "salty": 1, "bitter": 0, "spicy": 0.25, "cheese": 1, "cuisine": Cuisine.Italian},
    {"name": Name.Id2, "salty": 1, "bitter": 0.25, "spicy": 0.25, "cheese": 1, "cuisine": Cuisine.Italian},
    {"name": Name.Id3, "salty": 1, "bitter": 0, "spicy": 0.5, "cheese": 0.5, "cuisine": Cuisine.Polish},
    {"name": Name.Id4, "salty": 1, "bitter": 0, "spicy": 0.25, "cheese": 0, "cuisine": Cuisine.Japanese},
]
