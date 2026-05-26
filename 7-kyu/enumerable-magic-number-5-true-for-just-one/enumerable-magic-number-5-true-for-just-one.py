def one(xs, f): 
    return sum(1 for x in xs if f(x)) == 1