import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

from data import DataHandler, Dish
from compareVectors import getBest
from entropy import getBestFeature
from treeToPng import treeToPng


def ask_question(id_of_feature, user_v, feature_names_df):
    choice = input()

    if choice == "f":
        user_v[id_of_feature] = False
        return "f"
    elif choice == "t":
        user_v[id_of_feature] = True
        return "t"
    else:
        print(" IDK ")
        return "n"

dh = DataHandler()
data = dh.getDishesAndNamesVector()
feature_names = Dish.get_dish_variable_names()
feature_names_df = pd.DataFrame(feature_names)
answered = False
guessed = False
depth = 0

size_of_vector = len(feature_names)
user_v = pd.DataFrame([[None] * size_of_vector], columns=range(size_of_vector))

while not guessed:

    # entropy
    values_from_pairs = pd.DataFrame([pair[1] for pair in data])
    id_of_feature = getBestFeature(values_from_pairs)

    print(id_of_feature)

    # asking a question
    print("{} Czy wybrana potrawa jest {}".format(
        "  " * depth, list(feature_names_df.values)[id_of_feature]))

    answered = False
    while not answered:

        if ask_question(id_of_feature, user_v, feature_names_df) not in ["f", "t"]:
            # handle idk answer
            id_of_feature += 1  # TODO another best entropy, not implemented yet
        else:
            answered = True

    data = getBest(user_v, data, 0.5)
    print("dlugosc x_df", len(data))

    if len(data) == 1:
        print("Klasa końcowa:", data[0])
        guessed = True
