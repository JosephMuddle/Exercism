def rotate(text, key):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()
    if key == 0 or key == 26:
        return text
    else:
        return ''.join([alphabet_lower[(alphabet_lower.index(text[i])+key) % 26] if text[i] in alphabet_lower\
                    else alphabet_upper[(alphabet_upper.index(text[i])+key) % 26] if text[i] in alphabet_upper\
                        else text[i] for i in range(len(text))])
