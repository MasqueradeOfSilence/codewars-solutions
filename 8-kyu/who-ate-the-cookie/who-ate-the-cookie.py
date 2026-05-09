def cookie(x):
    culprit = "the dog"
    if isinstance(x, str):
        culprit = "Zach"
    if isinstance(x, float) or (isinstance(x, int) and not isinstance(x, bool)):
        culprit = "Monica"
    return "Who ate the last cookie? It was " + culprit + "!"