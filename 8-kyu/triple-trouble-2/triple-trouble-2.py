def triple_trouble(one, two, three):
    length = len(one)
    to_return = ""
    for i in range(0, length):
        to_return += one[i]
        to_return += two[i]
        to_return += three[i]
    return to_return