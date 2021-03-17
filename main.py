import random
import math
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import time

def estimate_pi(n):
    """Monte carlo estimation of pi; based on
    ratio between area in quarter circle vs unit square"""
    points_out = []
    points_in = []
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if math.sqrt(x**2 + y**2) <= 1:
            points_in.append((x,y))
        else:
            points_out.append((x,y))
    est_pi = (len(points_in) / (len(points_out) + len(points_in))) * 4
    return est_pi

# Plot the estimate vs number of samples
nsamples = [10, 30, 50, 80, 100, 200, 500, 700, 1e3, 2e3, 5e3, 7e3, 1e4]
estimates = []
for ns in nsamples:
    for tt in range(100):
        estimates.append([ns, estimate_pi(int(ns))])
df = pandas.DataFrame(estimates, columns=["num_samples", "est_pi"])
sns.lineplot(x="num_samples",
             y="est_pi",
             data=df)
plt.axhline(y=math.pi, color='k', linestyle="--")
plt.show()
