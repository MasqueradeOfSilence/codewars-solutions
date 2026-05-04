def count_letters_and_digits(s):
    num_alphanumeric = 0
    for el in s:
        if el.isalnum():
            num_alphanumeric += 1
    return num_alphanumeric