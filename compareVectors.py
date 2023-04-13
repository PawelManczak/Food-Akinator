from copy import copy

import numpy as np
import pandas as pd
from pandas import DataFrame


def compareVectors(user_v: DataFrame, v: DataFrame) -> float:
    v1 = pd.DataFrame(v).T
    neg_replacement_map = {True: -1, False: 1, None: None}
    replacement_map = {True: 1, False: -1, None: None}

    v1.replace(neg_replacement_map, inplace=True)
    user_v1 = copy(user_v)
    user_v1.replace(replacement_map, inplace=True)

    def sum_with_none(x, y):
        if x is None or y is None:
            return None
        else:
            return x + y

    result = v1.combine(user_v1, func=sum_with_none)

    sum_of_all_elements = np.nansum(result.values)
    num_of_null_values = user_v1.isnull().sum().sum()
    to_return = abs(sum_of_all_elements / (len(user_v1) - num_of_null_values))

    return to_return


def getBest(user_v: DataFrame, vectors: list, factor: float):
    best = [compareVectors(user_v, vector[1]) for vector in vectors]
    zipped = [pair + (value,) for pair, value in zip(vectors, best)]

    countZeros = best.count(0)
    # print("amount of zeros: ", countZeros)
    sorted_array = sorted(zipped, key=lambda x: x[2])

    size = round(len(vectors) * factor)

    if size < countZeros:
        size = countZeros

    sorted_array = sorted_array[:size]
    array_to_return = [item[:2] for item in sorted_array]
    best = [compareVectors(user_v, vector[1]) for vector in array_to_return]
    print("best: ", best)
    return array_to_return
