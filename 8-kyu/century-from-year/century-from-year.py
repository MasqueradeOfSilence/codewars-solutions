def century(year):
    if year <= 100:
        return 1
    year_str = str(year)
    if year_str[-1] == "0" and year_str[-2] == "0":
        return int(year_str[:-2])
    return int(year_str[:-2]) + 1