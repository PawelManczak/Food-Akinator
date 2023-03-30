from dataclasses import dataclass, fields


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

    def load_dishes(self):
        self.add_dish('pizza margherita', Dish(cheese=True, cuisineItalian=True))
        self.add_dish('pizza capriciosa',
                      Dish(sweet=False, sour=False, spicy=False, salty=False, umami=False, bitter=False, cheese=True,
                           gluten_free=False, vegetarian=False, vegan=False, organic=False, cuisineAmerican=False,
                           cuisineChinese=False, cuisineFrench=False, cuisineGreek=False, cuisineIndian=False,
                           cuisineItalian=True, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=False))
        self.add_dish('spaghetti bolognese',
                      Dish(sweet=False, sour=False, spicy=False, salty=False, umami=False, bitter=False, cheese=False,
                           gluten_free=False, vegetarian=False, vegan=False, organic=False, cuisineAmerican=False,
                           cuisineChinese=False, cuisineFrench=False, cuisineGreek=False, cuisineIndian=False,
                           cuisineItalian=True, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=False))
        self.add_dish('carbonara',
                      Dish(sweet=False, sour=False, spicy=False, salty=False, umami=False, bitter=False, cheese=True,
                           gluten_free=False, vegetarian=False, vegan=False, organic=False, cuisineAmerican=False,
                           cuisineChinese=False, cuisineFrench=False, cuisineGreek=False, cuisineIndian=False,
                           cuisineItalian=True, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=False))
        self.add_dish('lasagne',
                      Dish(sweet=False, sour=False, spicy=False, salty=False, umami=False, bitter=False, cheese=True,
                           gluten_free=False, vegetarian=False, vegan=False, organic=False, cuisineAmerican=False,
                           cuisineChinese=False, cuisineFrench=False, cuisineGreek=False, cuisineIndian=False,
                           cuisineItalian=True, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=False))
        self.add_dish('risotto',
                      Dish(sweet=False, sour=False, spicy=False, salty=False, umami=False, bitter=False, cheese=True,
                           gluten_free=False, vegetarian=False, vegan=False, organic=False, cuisineAmerican=False,
                           cuisineChinese=False, cuisineFrench=False, cuisineGreek=False, cuisineIndian=False,
                           cuisineItalian=True, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=False))
        self.add_dish('hamburger',
                      Dish(sweet=False, sour=False, spicy=False, salty=False, umami=False, bitter=False, cheese=True,
                           gluten_free=False, vegetarian=False, vegan=False, organic=False, cuisineAmerican=True,
                           cuisineChinese=False, cuisineFrench=False, cuisineGreek=False, cuisineIndian=False,
                           cuisineItalian=False, cuisineJapanese=False, cuisineKorean=False, cuisineMexican=False,
                           cuisineMiddle_Eastern=False, cuisineRussian=False, cuisineThai=False,
                           cuisineVietnamese=False, cuisineOther=False))
        self.add_dish('steak', Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('salmon fillet', Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('fish and chips',
                      Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=False))
        self.add_dish('chicken curry', Dish(sweet=False, spicy=True, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('beef stroganoff',
                      Dish(sweet=False, spicy=False, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('spinach and feta pie',
                      Dish(sweet=False, spicy=False, sour=False, bitter=True, salty=True, umami=False))
        self.add_dish('grilled cheese sandwich',
                      Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('hamburger', Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('chicken shawarma',
                      Dish(sweet=False, spicy=True, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('fajitas', Dish(sweet=False, spicy=True, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('taco salad', Dish(sweet=False, spicy=False, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('chicken teriyaki',
                      Dish(sweet=True, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('beef and broccoli stir fry',
                      Dish(sweet=False, spicy=False, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('vegetable lasagna',
                      Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('beef bourguignon',
                      Dish(sweet=False, spicy=False, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('shrimp scampi', Dish(sweet=False, spicy=False, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('lamb chops', Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('chicken cordon bleu',
                      Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('chicken alfredo',
                      Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('spaghetti bolognese',
                      Dish(sweet=False, spicy=False, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('pork ribs', Dish(sweet=True, spicy=True, sour=False, bitter=False, salty=True, umami=True))
        self.add_dish('beef kebab', Dish(sweet=False, spicy=True, sour=True, bitter=False, salty=True, umami=True))
        self.add_dish('grilled salmon',
                      Dish(sweet=False, spicy=False, sour=False, bitter=False, salty=True, umami=True))
