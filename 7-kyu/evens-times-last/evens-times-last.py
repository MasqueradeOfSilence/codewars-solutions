def even_last(numbers): 
    if len(numbers) == 0:
        return 0
    even_index_sum = sum(numbers[::2]) 
    return even_index_sum * numbers[-1]