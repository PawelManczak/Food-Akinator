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
x = dh.dishes
y = dh.names
x_df = pd.DataFrame(x)
y_df = pd.DataFrame(dh.names)

feature_names = Dish.get_dish_variable_names()
feature_names_df = pd.DataFrame(feature_names)
answered = False
guesed = False
depth = 0

size_of_vector = len(feature_names)

user_v = pd.DataFrame([[None]*size_of_vector], columns=range(size_of_vector))
#user_v = user_v.applymap(lambda _: None)

while not guesed:

    # entropy

    id_of_feature = getBestFeature(x_df)
    print(id_of_feature)

    # asking a question
    print("{} Czy wybrana potrawa jest {}".format(
        "  " * depth, list(feature_names_df.values)[id_of_feature]))
    answered = False
    while not answered:

        if ask_question(id_of_feature, user_v, feature_names_df) not in ["f", "t"]:
            # handle idk answer
            id_of_feature += 1 # TODO another best entropy, not implemented yet
        else:
            answered = True

    # reducing amount of possible answers
    user_v.iat[0, 0] = False
    print("debug \n")
    print(type(x_df))
    print(type(getBest(user_v, pd.DataFrame(x_df), 0.5)))
    x_df = getBest(user_v, x_df, 0.5)

    if len(x_df) == 1:
        # TODO tu trzeba ogarnac polaczenie x z y jakos
        print("Klasa końcowa:", x_df)
        answered = True
