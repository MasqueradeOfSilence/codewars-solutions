def longest(a1, a2):
    combined = a1 + a2
    alphabetical = "".join(sorted(combined))
    return "".join(dict.fromkeys(alphabetical))