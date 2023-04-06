import numpy as np
import pandas as pd
from pandas import DataFrame
from sqlalchemy import null
from data import DataHandler, Dish


def compareVectors(user_v: DataFrame, v: DataFrame) -> float:
    print(type(v))
    v1 = pd.DataFrame(v)
    v1 = v1.applymap(lambda x: -x if pd.notnull(x) else None)

    result = v1.add(user_v, fill_value=0).where((v1.notnull()) & (user_v.notnull()))
    sum_of_all_elements = result.dropna().sum().sum()
    num_of_null_values = user_v.isnull().sum().sum()
    to_return = abs(sum_of_all_elements / (len(user_v) - num_of_null_values))

    return to_return


def getBest(user_v: DataFrame, vectors: DataFrame, factor: float):
    best = [compareVectors(user_v, vector) for vector in vectors]
    best.sort()
    return best[:round(len(user_v) * factor)]


"""user = pd.DataFrame([True, False, None])

df2 = pd.DataFrame([True, False, True])

result = compareVectors(df2, user)
print(result)

dh = DataHandler()

x = dh.dishes
y = dh.names
x_df = pd.DataFrame(x)
y_df = pd.DataFrame(dh.names)

print(type(pd.DataFrame(x[0])))

print("----- same -------")
print(compareVectors(pd.DataFrame(x[0]), pd.DataFrame(x[0])))
print(getBest(pd.DataFrame(x[0]), x, 0.5))"""
