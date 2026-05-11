def open_or_senior(data):
    to_return = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            to_return.append("Senior")
        else:
            to_return.append("Open")
    return to_return