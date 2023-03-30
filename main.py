from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_text
from database import database
from data import SetUpData

# enums
# DecisionTreeClassifier() cannot work on strings, so we need to set to each of them identifier,
# we should make it programmatically

# creating a list from database structure
values_list = []
for recipe in database:
    values = list(recipe.values())
    values_list.append(values)

#print(values_list)

# creating a decision tree
x = values_list
y = list(range(0, len(x)))

tree_clf = DecisionTreeClassifier()
tree_clf.fit(x, y)

# visualization
features = list(database[0].keys())
f = open("iris_tree.dot", 'w')
export_graphviz(
    tree_clf,
    out_file=f,  # path where you want it to output
    feature_names=features,
    class_names=list(map(str, y)),
    rounded=True,
    filled=True
)

r = export_text(tree_clf)
#print(r)
example = SetUpData('some string', sweet=True, spicy=True)
print(example)
# dot -Tpng iris_tree.dot -o iris_tree.png <-- command exporting to png
