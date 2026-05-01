def mean(lst):
    total = 0
    concatenated = ""
    for el in lst:
        if el.isalpha():
            concatenated = concatenated + el 
        else:
            total = total + int(el)
    avg = total / 10
    return [avg, concatenated]
    