def high_and_low(numbers):
    num_array = [int(x) for x in numbers.split()]
    return f"{max(num_array)} {min(num_array)}"