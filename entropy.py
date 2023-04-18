import math


def countp(df):
    # count how many times one has been spotted in a column
    p_vector = []
    for _ in range(len(df.columns)):
        p_vector.append(0)
    for column, values in df.items():
        for value in values:
            if value == True:
                p_vector[column] += 1
    return p_vector


def countEntropy(df):
    # E=-(-p/all*log2(p/all)-(all-p)/all*log2((all-p)/all)))
    p_vector = countp(df)
    allFeatures = len(p_vector)
    entropy = []
    max_value = len(df)
    for _ in range(allFeatures):
        entropy.append(0)
    for i in range(allFeatures):
        p = p_vector[i]
        if p == 0 or p == max_value:
            entropy[i] = 0
        else:
            entropy[i] = -(p / max_value * math.log(p / max_value, 2) + ((max_value - p) / max_value) * math.log(
                (max_value - p) / max_value, 2))
    return entropy


def countGini(df):
    p_vector = countp(df)
    allFeatures = len(p_vector)
    gini = []
    max_value = len(df)
    for _ in range(allFeatures):
        gini.append(0)
    for i in range(allFeatures):
        p = p_vector[i]
        if p == 0 or p == max_value:
            gini[i] = 0
        else:
            gini[i] = 1-((p / max_value)**2 + ((max_value - p) / max_value)**2)
    return gini


def getBestFeature(df):
    entropy_vector = countEntropy(df)
    index = -1
    maxValue = -1
    for i in range(len(entropy_vector)):
        if entropy_vector[i] > maxValue:
            maxValue = entropy_vector[i]
            index = i
    return index

def getBestFeatureGini(df):
    entropy_vector = countGini(df)
    index = -1
    maxValue = -1
    for i in range(len(entropy_vector)):
        if entropy_vector[i] > maxValue:
            maxValue = entropy_vector[i]
            index = i
    return index
