def time_overlap(t1_start, t1_end, t2_start, t2_end):
    return max(t1_start, t2_start) <= min(t1_end, t2_end)
