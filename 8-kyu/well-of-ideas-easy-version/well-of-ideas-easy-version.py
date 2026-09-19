def well(x):
    good = x.count("good")
    bad = x.count("bad")
    if good < 3 and good > 0:
        return "Publish!"
    elif good > 2:
        return "I smell a series!"
    return "Fail!"