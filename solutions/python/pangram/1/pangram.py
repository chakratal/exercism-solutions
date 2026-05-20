def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if len(sentence) >= 26:
        for letter in alphabet:
            if letter not in sentence.lower():
                return False
        return True
    return False