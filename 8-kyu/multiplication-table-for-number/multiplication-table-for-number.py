def multi_table(number):
    to_return = ""
    for i in range(1, 11):
        if i == 10:
            to_return += (f"{i} * {number} = {i * number}")
        else:
            to_return += (f"{i} * {number} = {i * number}\n")
    return to_return