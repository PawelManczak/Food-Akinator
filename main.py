from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_text

from data import DataHandler, Dish

dh = DataHandler()
# dh.serializeData(Dish)
# creating a decision tree
x = dh.dishes
y = dh.names
print(len(x))
tree_clf = DecisionTreeClassifier(criterion='entropy', min_samples_leaf=1, max_depth=100000)
tree_clf.fit(x, y)

# visualization
f = open("iris_tree.dot", 'w')
export_graphviz(
    tree_clf,
    out_file=f,  # path where you want it to output
    feature_names=Dish.get_dish_variable_names(),
    class_names=y,
    rounded=True,
    filled=True
)

r = export_text(tree_clf)
print(r)

children_left = tree_clf.tree_.children_left
children_right = tree_clf.tree_.children_right

#print(tree_clf.tree_.feature[6])
# pobieramy tablice z indeksami atrybutów i wartościami progów
features = tree_clf.tree_.feature
thresholds = tree_clf.tree_.threshold


# wyświetlamy warunki różnicujące dla węzłów

# # funkcja rekurencyjna do wypisania węzłów
def print_node(node_id, depth):
    # wypisujemy węzeł

    if children_left[node_id] == -1 or children_right[node_id] == -1:

        predicted_class = tree_clf.classes_[tree_clf.tree_.value[node_id][0].argmax()]
        print("Klasa końcowa:", predicted_class)

    else:

        choice = "L"

        while(choice != "t" and choice != "f"):
            print("{}{}. Czy wybrana potrawa jest {}".format(
                "  " * depth, node_id, Dish.get_dish_variable_names()[features[node_id]], thresholds[node_id]))
            # przechodzimy do lewego i prawego potomka, jeśli istnieją

            choice = input()

            if choice == "f":
                print_node(children_left[node_id], depth + 1)
            elif choice == "t":
                print_node(children_right[node_id], depth + 1)

print_node(0, 0)