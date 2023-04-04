import pandas as pd

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.tree import export_text

from data import DataHandler, Dish


def treeToPng(tree_clf, feature_names, y):
    f = open("iris_tree.dot", 'w')
    export_graphviz(
        tree_clf,
        out_file=f,  # path where you want it to output
        feature_names=feature_names,
        class_names=y,
        rounded=True,
        filled=True
    )


# dot -Tpng iris_tree.dot -o iris_tree.png <-- command exporting to png