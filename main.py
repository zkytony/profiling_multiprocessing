import random
import math
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
import time
import multiprocessing as mp
import numpy as np
import progressbar

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

def estimate_pi_multi_proc(n, nproc=4):
    n_per = int(round(n / nproc))
    pool = mp.Pool(nproc)
    with pool:
        return(np.mean(pool.map(estimate_pi, [n_per]*nproc)))

def plot_estimates():
    # Plot the estimate vs number of samples
    nsamples = [10, 30, 50, 80, 100, 200, 500, 700, 1e3, 2e3, 5e3, 7e3, 1e4]
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
            est_pi_mp = estimate_pi_multi_proc(int(ns), nproc=4)
            time_est_pi_mp = time.time() - _start
            estimates.append(["multi", ns, est_pi_mp, time_est_pi_mp])

        bar.finish()

    df = pandas.DataFrame(estimates, columns=["type", "num_samples", "est_pi", "time"])

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
    sns.lineplot(x="num_samples",
                 y="est_pi",
                 hue="type",
                 data=df,
                 ax=axes[0])
    axes[0].axhline(y=math.pi, color='k', linestyle="--")

    sns.lineplot(x="num_samples",
                 y="time",
                 hue="type",
                 data=df,
                 ax=axes[1])
    fig.savefig("plot.png")

# estimate_pi_multi_proc(1e5, nproc=8)
plot_estimates()
