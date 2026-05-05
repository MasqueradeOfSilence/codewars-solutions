from collections import Counter
def ordered_count(inp):
    counts = Counter(inp)
    return list(counts.items())