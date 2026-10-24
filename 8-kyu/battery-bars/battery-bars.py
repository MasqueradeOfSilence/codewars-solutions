import math
def battery_bars(percent):
    numPounds = math.floor(percent / 20)
    pounds = "#" * numPounds
    numPeriods = 5 - numPounds
    periods = "." * numPeriods
    return f"[{pounds}{periods}]"