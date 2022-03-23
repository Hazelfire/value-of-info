import numpy as np

card_count = 7
round_to_nearest = 5

def my_round(x):
    return np.around(x/5, decimals=0) * 5
standard_deviation = 10

for i in range(card_count):
    print("Intervention {}".format(i))
    mean = my_round(np.random.normal(70, standard_deviation))
    width = my_round(np.abs(np.random.normal(20, 5)))
    low_score = mean - width
    high_score = mean + width

    print("{}U - {}U".format(low_score, high_score))

    mean = (low_score + high_score) / 2
    sd = (high_score - mean)/1.6
    actual = my_round(np.random.normal(mean, sd))
    print("Actual: {}U".format(actual))

