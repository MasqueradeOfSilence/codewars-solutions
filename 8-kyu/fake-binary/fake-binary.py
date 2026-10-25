def fake_bin(x):
    return ''.join('1' if ord(char) - ord('0') >= 5 else '0' for char in x)