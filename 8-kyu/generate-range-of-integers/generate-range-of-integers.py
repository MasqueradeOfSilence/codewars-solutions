def generate_range(start, stop, step):
    to_ret = []
    for i in range(start, stop + 1, step):
        to_ret.append(i)
    return to_ret