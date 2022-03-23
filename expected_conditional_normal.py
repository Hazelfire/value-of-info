import sys
import numpy as np

mean = float(sys.argv[1])
sd = float(sys.argv[2]) / 3.2
portion = sys.argv[3]
conditional = float(sys.argv[4])
samples = 10000

results = []

for i in range(samples):
    result = np.random.normal(mean, sd)
    if portion == "lower" and result < conditional:
        results.append(result)
    elif portion == "higher" and result > conditional:
        results.append(result)

mean = np.mean(results)
prob = len(results)/samples
vpi = mean * prob

print("Expected {}. Probability {}. VPI: {}".format(mean, prob, vpi))
