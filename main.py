from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_text

from data import DataHandler, Dish

dh = DataHandler()
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

features = tree_clf.tree_.feature
thresholds = tree_clf.tree_.threshold


# wyświetlamy warunki różnicujące dla węzłów

# funkcja rekurencyjna do wypisania węzłów
node = 0  # zaczynamy od korzenia
while tree_clf.tree_.children_left[node] != tree_clf.tree_.children_right[node]:
    feature = tree_clf.tree_.feature[node]
    threshold = tree_clf.tree_.threshold[node]
    answer = input("Czy {} <= {}? ".format(Dish.get_dish_variable_names()[features[node]], threshold))
    if answer == 't':
        node = tree_clf.tree_.children_left[node]
    else:
        node = tree_clf.tree_.children_right[node]

predicted_class = tree_clf.classes_[tree_clf.tree_.value[node][0].argmax()]

print("Klasa końcowa:", predicted_class)
dh.serializeData(Dish)
# dot -Tpng iris_tree.dot -o iris_tree.png <-- command exporting to png
