import numpy as np
import pandas as pd
from pandas import DataFrame
from sqlalchemy import null


def compareVectors(user_v: DataFrame, v: DataFrame) -> float:
    v1 = v

    v1 = v1.applymap(lambda x: -x if pd.notnull(x) else None)

    result = v1.add(user_v, fill_value=0).where((v1.notnull()) & (user_v.notnull()))
    sum_of_all_elements = result.dropna().sum().sum()
    num_of_null_values = user_v.isnull().sum().sum()
    to_return = abs(sum_of_all_elements / (len(user_v) - num_of_null_values))

    return to_return


user = pd.DataFrame([True, False, None])

df2 = pd.DataFrame([True, False, True])

result = compareVectors(df2, user)
print(result)
