def count_consonants(text):
    vowels = "aeiou"
    text = text.lower()
    text = "".join(dict.fromkeys(text))
    return len([ch for ch in text if ch not in vowels and ch.isalpha()])