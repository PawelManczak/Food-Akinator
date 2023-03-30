from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_text

from data import DataHandler, Dish

dh = DataHandler()

# creating a decision tree
x = dh.dishes
y = dh.names

tree_clf = DecisionTreeClassifier()
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

# dot -Tpng iris_tree.dot -o iris_tree.png <-- command exporting to png
