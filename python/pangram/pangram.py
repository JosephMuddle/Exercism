def is_pangram(sentence):
    letters = (''.join(filter(str.isalpha, sentence))).lower()
    return len(set(letters)) == 26