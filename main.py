import pandas as pd

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_text

from data import DataHandler, Dish

dh = DataHandler()
# dh.serializeData(Dish)
# creating a decision tree
x = dh.dishes
y = dh.names
x_df = pd.DataFrame(x)
y_df = pd.DataFrame(dh.names)
counter = 0
print(len(x))
feature_names = Dish.get_dish_variable_names()
feature_names_df = pd.DataFrame(feature_names)
answered = False
x_df = x_df.iloc[1:].reset_index(drop=True)
y_df = y_df.iloc[1:].reset_index(drop=True)
x_df.columns = x_df.columns.astype(str)

while not answered:
    tree_clf = DecisionTreeClassifier(criterion='entropy', min_samples_leaf=1)
    tree_clf.fit(x_df, y_df)

    # visualization
    f = open("iris_tree.dot", 'w')
    export_graphviz(
        tree_clf,
        out_file=f,  # path where you want it to output
        feature_names=feature_names,
        class_names=y,
        rounded=True,
        filled=True
    )
    r = export_text(tree_clf)
    # print(r)

    children_left = tree_clf.tree_.children_left
    children_right = tree_clf.tree_.children_right

    # print(tree_clf.tree_.feature[6])
    # pobieramy tablice z indeksami atrybutów i wartościami progów
    features = tree_clf.tree_.feature
    thresholds = tree_clf.tree_.threshold


    # wyświetlamy warunki różnicujące dla węzłów

    # # funkcja rekurencyjna do wypisania węzłów
    def print_node(node_id, depth):
        global x, counter, feature_names_df, x_df, answered, feature_names
        # wypisujemy węzeł
        if children_left[node_id] == -1 or children_right[node_id] == -1:

            predicted_class = tree_clf.classes_[tree_clf.tree_.value[node_id][0].argmax()]
            print("Klasa końcowa:", predicted_class)
            answered = True

        else:

            choice = "L"

            while choice != "t" and choice != "f":
                print("{}{}. Czy wybrana potrawa jest {}".format(
                    "  " * depth, node_id, list(feature_names_df.values)[features[node_id]]))
                # przechodzimy do lewego i prawego potomka, jeśli istnieją

                choice = input()

                if choice == "f":
                    print_node(children_left[node_id], depth + 1)
                elif choice == "t":
                    print_node(children_right[node_id], depth + 1)
                else:

                    # usuwanie kolumny z feature_names_x i x _df

                    column_to_remove = features[node_id]  # indeks kolumny do usunięcia
                    feature_names = [f for i, f in enumerate(feature_names) if i != column_to_remove]
                    feature_names_df = pd.DataFrame(feature_names)

                    x_df = x_df.drop(str(column_to_remove), axis=1).reset_index(drop=True)
                    x_df.columns = x_df.columns.astype(int)

                    new_headers = [i for i in range(len(x_df.columns))]

                    # zmiana nazw kolumn na nowe nagłówki
                    x_df = x_df.rename(columns=dict(zip(x_df.columns, new_headers)))
                    x_df.columns = x_df.columns.astype(str)
                    return


    print_node(0, 0)

# dot -Tpng iris_tree.dot -o iris_tree.png <-- command exporting to png
