from enum import IntEnum


class Cuisine(IntEnum):
    Italian = 1
    Polish = 2
    Japanese = 3


class Name(IntEnum):
    Id1 = 1.
    Id2 = 2.
    Id3 = 3.
    Id4 = 4.


# there should be a class Dish, each of dish must have same features, also when it is set to zero
database = [
    {"name": Name.Id1, "salty": True, "bitter": False, "spicy": True, "cheese": False, "cuisine": Cuisine.Italian},
    {"name": Name.Id2, "salty": True, "bitter": False, "spicy": False, "cheese": False, "cuisine": Cuisine.Italian},
    {"name": Name.Id3, "salty": True, "bitter": False, "spicy": True, "cheese": True, "cuisine": Cuisine.Italian},
    {"name": Name.Id4, "salty": True, "bitter": False, "spicy": False, "cheese": True, "cuisine": Cuisine.Italian},
    {"name": Name.Id2, "salty": False, "bitter": False, "spicy": True, "cheese": True, "cuisine": Cuisine.Italian},
    {"name": Name.Id3, "salty": False, "bitter": False, "spicy": False, "cheese": True, "cuisine": Cuisine.Polish},
    {"name": Name.Id4, "salty": True, "bitter": False, "spicy": False, "cheese": False, "cuisine": Cuisine.Japanese},
]


