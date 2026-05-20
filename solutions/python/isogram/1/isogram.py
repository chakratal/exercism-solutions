def is_isogram(string):
    return sorted(list(set(string.lower().replace("-", "").replace(" ", "")))) == sorted(string.lower().replace("-", "").replace(" ", ""))