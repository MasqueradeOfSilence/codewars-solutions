def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence.lower() if char in vowels)