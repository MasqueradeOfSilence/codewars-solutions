def sum_factorial(lst):
    total = 0
    for el in lst:
        result = 1
        for i in range(2, el + 1):
            result *= i
        total += result
    return total
​
'''
    Notes: 
        A factorial is obtained by n! = n * (n-1) * (n-2) * ... * 1.
'''