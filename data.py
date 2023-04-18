from dataclasses import dataclass, fields
from dataSQL import serialize, deserialize

@dataclass
class Dish:
    sweet: bool = False
    sour: bool = False
    spicy: bool = False
    salty: bool = False
    umami: bool = False
    bitter: bool = False
    cheese: bool = False
    vegetarian: bool = False
    cuisineAmerican: bool = False
    cuisineIndian: bool = False
    cuisineItalian: bool = False
    cuisineJapanese: bool = False
    cuisineMexican: bool = False
    fish: bool = False
    tomato: bool = False
    mostlyMeet: bool = False
    pasta: bool = False

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

    def set_none(self):

        for arg in fields(self):
            a = str(arg.name)
            self.__dict__[a] = None

    def update(self,dish):

        for arg in fields(self):
            a = str(arg.name)
            if self.__dict__[a] == None:
                self.__dict__[a] = dish.__dict__[a]

    def get_value(self,index):
        i = 0
        wartosc = None
        for arg in fields(self):
            if i == index:
                a = str(arg.name)
                wartosc = self.__dict__[a]
            i = i+1
        return wartosc


class DataHandler:
    names: list[str] = []
    dishes = []

    def add_dish(self, name: str, dish: Dish):
        self.names.append(name)
        self.dishes.append(dish.get_dish_vector())

    def __init__(self):
        self.load_dishes()

    def getDishesAndNamesVector(self):
        return list(zip(self.names, self.dishes))
    def serializeData(self, Dish):
        serialize(self, Dish)


    def deserializeData(self, Dish):
        deserialize(self, Dish)

    def update_dish(self,dish,new_answers):

        for i in range(0,len(self.names)):
            if self.names[i] == dish[0]:
                for j in range(0,len(self.dishes[i])):
                    if self.dishes[i][j] == None:
                        self.dishes[i][j] = new_answers.get_value(j)


    def load_dishes(self):
        self.add_dish('pizza margherita', Dish(sweet=True, sour=True, spicy=True))
        self.add_dish('pizza', Dish(cheese=True, salty=True, cuisineItalian=True))
        self.add_dish('carbonara', Dish(cheese=True, salty=True, cuisineItalian=True, pasta=True))
        self.add_dish('lasagne', Dish(salty=True, cheese=True, tomato=True, pasta=True))
        self.add_dish('risotto', Dish(salty=True, cheese=True, cuisineItalian=True))
        self.add_dish('steak', Dish(salty=True, mostlyMeet=True))
        self.add_dish('salmon fillet', Dish(salty=True, umami=True, fish=True))
        self.add_dish('fish and chips', Dish(salty=True, fish=True))
        self.add_dish('chicken curry', Dish(spicy=True, salty=True, umami=True, cuisineIndian=True))
        self.add_dish('beef stroganoff', Dish(sour=True, salty=True, umami=True, mostlyMeet=True))
        self.add_dish('spinach and feta pie', Dish(bitter=True, salty=True))
        self.add_dish('grilled cheese sandwich', Dish(cheese=True, salty=True, umami=True, vegetarian=True))
        self.add_dish('hamburger', Dish(salty=True, cuisineAmerican=True, tomato=True))
        self.add_dish('fajitas', Dish(spicy=True, sour=True, salty=True, umami=True, cuisineMexican=True))
        self.add_dish('taco salad', Dish(sour=True, salty=True, umami=True, tomato=True, cuisineMexican=True))
        self.add_dish('chicken teriyaki', Dish(sweet=True, salty=True, umami=True, cuisineJapanese=True, mostlyMeet=True))
        self.add_dish('vegetable lasagna', Dish(salty=True, cuisineItalian=True, vegetarian=True, tomato=True, pasta=True))
        self.add_dish('shrimp scampi', Dish(sour=True, salty=True, cuisineItalian=True))
        self.add_dish('lamb chops', Dish(salty=True, umami=True, mostlyMeet=True))
        self.add_dish('spaghetti bolognese', Dish(sour=True, salty=True, umami=True, tomato=True))
        self.add_dish('pork ribs', Dish(sweet=True, spicy=True, salty=True, umami=True, mostlyMeet=True))
        self.add_dish('kebab', Dish(spicy=True, sour=True, salty=True, umami=True, cuisineIndian=True))