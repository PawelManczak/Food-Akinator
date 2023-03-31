from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_text

from data import DataHandler, Dish

dh = DataHandler()

# creating a decision tree
x = dh.dishes
y = dh.names

tree_clf = DecisionTreeClassifier(criterion='entropy')
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
#print(r)

children_left = tree_clf.tree_.children_left
children_right = tree_clf.tree_.children_right

print(tree_clf.tree_.feature[6])
# pobieramy tablice z indeksami atrybutów i wartościami progów
features = tree_clf.tree_.feature
thresholds = tree_clf.tree_.threshold


# funkcja rekurencyjna do wypisania węzłów
"""def print_node(node_id, depth):
    # wypisujemy węzeł
    print("{}node={}, feature={}, threshold={}".format(
        "  " * depth, node_id, features[node_id], thresholds[node_id]))
    # przechodzimy do lewego i prawego potomka, jeśli istnieją
    if children_left[node_id] != -1:
        print_node(children_left[node_id], depth + 1)
    if children_right[node_id] != -1:
        print_node(children_right[node_id], depth + 1)


# wywołujemy funkcję dla korzenia drzewa
print_node(0, 0)
# walking through tree"""

# dot -Tpng iris_tree.dot -o iris_tree.png <-- command exporting to png
