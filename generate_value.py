import numpy as np
import random

card_count = 100
round_to_nearest = 5

def my_round(x):
    return np.around(x/5, decimals=0) * 5
standard_deviation = 10

def gen_charity_name():
    cause_area = ""
    if random.random() > 0.5:
        bad_thing = random.choice(["Blindness", "Apocolypse", "Nuclear War", "Malaria", "Measles", "Poverty", "Stupidity", "Worms", "Hunger", "Bioweapons", "Depression", "Guns", "Fascism", "Cancer", "Aging", "Inefficiency", "Suffering", "Mediocrity", "Overpopulation", "Climate Change", "Power Conflict", "Surveillance"])
        negation = random.choice(["Action Against {}", "Against {}", "{} Prevention", "Anti {}"])
        cause_area = negation.format(bad_thing)
    else:
        moral_patients = random.choice(["AI", "Humans", "Children", "Fish", "Kittens", "Insects", "Pidgeons", "Grandmothers", "Doggos", "Infants", "Earth", "Trees", "Bourgeoisie", "Economists", "Effective Altruists", "Democracy", "Rationalists", "Wild Animals", "Students", "Women"])
        good_actions = random.choice(["{} Welfare", "Save The {}", "{} Happiness", "Help the {}", "{} Defence", "{} Protection", "{} Conservation", "Remember the {}"])
        if random.random() < 0.9:
            cause_area = good_actions.format(moral_patients)
        else:
            cause_area = random.choice(["Global Priorities", "Nuclear Safety", "AI Safety", "Good Decisions", "Space Governence", "Quality Education", "Positivity", "Economic Growth"])

    if random.random() < 0.2:
        modifier = random.choice(["{} International", "Global {}", "{} Now", "Effective {}", "The {}", "Christian's {}"])
        cause_area = modifier.format(cause_area)

    org = random.choice(["Foundation", "Organization", "Consortium", "International", "Fund", "Agency", "Aid", "Initiative", "Research Institute", "Alliance", "Association", ""])
    name = "{} {}".format(cause_area, org)
    return name




def gen_charity():
    mean = np.random.normal(50, standard_deviation)
    width = np.abs(np.random.normal(20, 5))
    low_score = my_round(mean - width)
    high_score = my_round(mean + width)


    mean = (np.log(high_score) + np.log(low_score)) / 2
    sd = (np.log(high_score) - np.log(low_score)) / (1.6 * 2)
    actual = my_round(np.random.lognormal(mean, sd))

    return {'low': low_score, 'high': high_score, 'actual': actual, 'name': gen_charity_name()}



inside = 0
for i in range(card_count):
    results = gen_charity()
    print(results)
    if results['low'] < results['actual'] and results['actual'] < results['high']:
        inside += 1
