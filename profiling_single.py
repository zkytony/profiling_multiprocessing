# Run: python profiling_single.py
from viztracer import VizTracer
from estimate_pi_multi_proc import estimate_pi, estimate_pi_multi_proc

num_samples = 100
with VizTracer(output_file="single_thread.html") as tracer:
    estimate_pi(num_samples)
