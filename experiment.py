import random
import math
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import time
import numpy as np
import progressbar
from estimate_pi_multi_proc import estimate_pi, estimate_pi_multi_proc

def plot_estimates():
    # Plot the estimate vs number of samples
    #10, 30, 50] #80, 100, 200, 500, 700, 1e3, 2e3, 5e3, 7e3, 1e4]
    nsamples = [100, 300, 500, 700, 1e3, 1e4, 3e4, 5e4, 7e4, 1e5, 3e5, 5e5, 7e5, 1e6]
    estimates = []
    for ns in nsamples:

        print("Num samples %d" % ns)
        num_rounds = 100
        bar = progressbar.ProgressBar(
            maxval=num_rounds, \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()

        for tt in range(num_rounds):
            bar.update(tt+1)
            _start = time.time()
            est_pi = estimate_pi(int(ns))
            time_est_pi = time.time() - _start
            estimates.append(["single", ns, est_pi, time_est_pi])

            _start = time.time()
            est_pi_mp = estimate_pi_multi_proc(int(ns), nproc=8)
            time_est_pi_mp = time.time() - _start
            estimates.append(["multi", ns, est_pi_mp, time_est_pi_mp])

        bar.finish()

    df = pandas.DataFrame(estimates, columns=["type", "num_samples", "est_pi", "time"])

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18,9))
    sns.lineplot(x="num_samples",
                 y="est_pi",
                 hue="type",
                 data=df,
                 ax=axes[0])
    axes[0].axhline(y=math.pi, color='k', linestyle="--")
    axes[0].set_ylim(3.12, 3.16)

    sns.lineplot(x="num_samples",
                 y="time",
                 hue="type",
                 data=df,
                 ax=axes[1])
    fig.savefig("plot.png")

plot_estimates()
