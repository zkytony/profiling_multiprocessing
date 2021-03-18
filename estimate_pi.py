import random
import math

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
