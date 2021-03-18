import random
import math

def estimate_pi(n):
    """Monte carlo estimation of pi; based on
    ratio between area in quarter circle vs unit square"""
    points_out = 0
    points_in = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if math.sqrt(x**2 + y**2) <= 1:
            points_in += 1
        else:
            points_out += 1
    est_pi = (points_in / (points_out + points_in)) * 4
    return est_pi
