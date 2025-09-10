def find_len_string(text):
    return len(text.split())

def find_num_char(text):
    res = {}
    for char in text:
        c = char.lower()
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res
