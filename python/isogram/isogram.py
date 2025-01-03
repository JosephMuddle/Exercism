def is_isogram(string):
    return len(set((''.join(filter(str.isalpha, string))).lower())) == len((''.join(filter(str.isalpha, string))).lower())