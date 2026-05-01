import math
def sum_average(arr):
    total = 0
    for subarr in arr:
        avg = sum(subarr) / len(subarr)
        total += avg
    return math.floor(total)