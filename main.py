import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

from data import DataHandler, Dish
from compareVectors import getBest
from entropy import getBestFeature
from treeToPng import treeToPng


def ask_question(id_of_feature, user_v, feature_names_df,dish):
    choice = input()

    if choice == "f":
        dish.__dict__[list(feature_names_df)[id_of_feature]] = False
        user_v[id_of_feature] = False
        return "f"
    elif choice == "t":
        dish.__dict__[list(feature_names_df)[id_of_feature]] = True
        user_v[id_of_feature] = True
        return "t"
    else:
        print(" IDK ")
        return "n"

def add_new(dish,data):

    nazwa_final = ""
    print("Podaj nazwe potrawy o ktorej myslales")
    nazwa_final = input()
    data.add_dish(nazwa_final,dish)


dh = DataHandler()
dh.deserializeData(Dish)

data = dh.getDishesAndNamesVector()
feature_names = Dish.get_dish_variable_names()
feature_names_df = pd.DataFrame(feature_names)
answered = False
guessed = False
depth = 0

size_of_vector = len(feature_names)
user_v = pd.DataFrame([[None] * size_of_vector], columns=range(size_of_vector))

#pusty dish aktualizowany po kazdym pytaniu
act_dish = Dish()
act_dish.set_none()

while not guessed:

    # entropy
    values_from_pairs = pd.DataFrame([pair[1] for pair in data])
    id_of_feature = getBestFeature(values_from_pairs)

    print(id_of_feature)

    # asking a question
    print("{} Czy wybrana potrawa jest {}".format(
        "  " * depth, list(feature_names)[id_of_feature]))

    answered = False
    while not answered:

        if ask_question(id_of_feature, user_v, feature_names,act_dish) not in ["f", "t"]:
            # handle idk answer
            feature_names.pop(id_of_feature)
            for item in data:
                item[1].pop(id_of_feature)

            break
        else:
            answered = True
            data = getBest(user_v, data, 0.5)
            print("dlugosc x_df", len(data))

    if len(data) == 1:
        print("Klasa końcowa:", data[0])
        guessed = True
        print("Czy o to ci chodzio?")
        choice = input()
        if choice == "f":
            add_new(act_dish,dh)
        else:
            dh.update_dish(data[0],act_dish)
            print("koniec")

dh.serializeData(Dish)

