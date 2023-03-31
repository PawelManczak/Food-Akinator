from dataclasses import dataclass, fields
from dataSQL import serialize

@dataclass
class Dish:
    sweet: bool = False
    sour: bool = False
    spicy: bool = False
    salty: bool = False
    umami: bool = False
    bitter: bool = False
    cheese: bool = False
    gluten_free: bool = False
    vegetarian: bool = False
    vegan: bool = False
    organic: bool = False
    cuisineAmerican: bool = False
    cuisineChinese: bool = False
    cuisineFrench: bool = False
    cuisineGreek: bool = False
    cuisineIndian: bool = False
    cuisineItalian: bool = False
    cuisineJapanese: bool = False
    cuisineKorean: bool = False
    cuisineMexican: bool = False
    cuisineMiddle_Eastern: bool = False
    cuisineRussian: bool = False
    cuisineThai: bool = False
    cuisineVietnamese: bool = False
    cuisineOther: bool = False
    fruity: bool = False
    nutty: bool = False
    herbal: bool = False
    floral: bool = False
    earthy: bool = False
    cheesy: bool = False
    creamy: bool = False
    smoky: bool = False
    savory: bool = False

    def __post_init__(self):
        true_args = [arg for arg in locals() if arg]
        if len(true_args) == 0:
            raise ValueError("At least one bool argument must be True.")

    def get_dish_vector(dish):
        dish_fields = fields(Dish)
        return [getattr(dish, field.name) for field in dish_fields]

    @staticmethod
    def get_dish_variable_names():
        dish_fields = fields(Dish)
        return [field.name for field in dish_fields]


class DataHandler:
    names: list[str] = []
    dishes = []

    def add_dish(self, name: str, dish: Dish):
        self.names.append(name)
        self.dishes.append(dish.get_dish_vector())

    def __init__(self):
        self.load_dishes()


    def serializeData(self, Dish):
        serialize(self, Dish)


    def load_dishes(self):
        self.add_dish('steak',
                      Dish(sweet=False, sour=False, bitter=False, salty=True, umami=True, spicy=False, fruity=False,
                           nutty=False, herbal=False, floral=False, earthy=False, cheesy=False, creamy=False,
                           smoky=False, savory=False))
        self.add_dish('salmon fillet',
                      Dish(sweet=False, sour=False, bitter=False, salty=True, umami=True, spicy=False, fruity=False,
                           nutty=False, herbal=False, floral=False, earthy=False, cheesy=False, creamy=False,
                           smoky=True, savory=False))
        self.add_dish('fish and chips',
                      Dish(sweet=False, sour=False, bitter=False, salty=True, umami=False, spicy=False, fruity=False,
                           nutty=False, herbal=False, floral=False, earthy=False, cheesy=False, creamy=False,
                           smoky=False, savory=False, cuisineChinese=False, cuisineFrench=False, cuisineGreek=False,
                           cuisineIndian=False,
                           cuisineItalian=True, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=False))
        self.add_dish('beef stroganoff',
                      Dish(sweet=False, sour=True, bitter=False, salty=True, umami=True, spicy=False, fruity=False,
                           nutty=False, herbal=False, floral=False, earthy=False, cheesy=False, creamy=True,
                           smoky=False, savory=False, cuisineIndian=False,
                           cuisineItalian=False, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=True))
        self.add_dish('spinach and feta pie',
                      Dish(sweet=False, sour=False, bitter=True, salty=True, umami=False, spicy=False, fruity=False,
                           nutty=True, herbal=False, floral=False, earthy=False, cheesy=True, creamy=False, smoky=False,
                           savory=False, cuisineIndian=False,
                           cuisineItalian=False, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=True))




