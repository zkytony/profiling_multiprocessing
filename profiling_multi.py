# Run: viztracer profiling_multi.py --log_multiprocess --output_file multi_proc_4.html
from estimate_pi_multi_proc import estimate_pi, estimate_pi_multi_proc
num_samples = 100
estimate_pi_multi_proc(num_samples, nproc=4)
