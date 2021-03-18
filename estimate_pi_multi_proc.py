from estimate_pi import estimate_pi
import multiprocessing as mp

def estimate_pi_multi_proc(n, nproc=4):
    n_per = int(round(n / nproc))
    pool = mp.Pool(nproc)
    with pool:
        return(sum(pool.map(estimate_pi, [n_per]*nproc)) / nproc)
