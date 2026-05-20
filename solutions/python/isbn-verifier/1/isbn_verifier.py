def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) < 10 or len(isbn) > 10:
        return False
    alphabet = "abcdefghijklmnopqrstuvwyz"
    for letter in alphabet:
        if letter in isbn.lower() or "x" in isbn.lower()[0:8]:
            return False
    if isbn[9] == "x" or isbn[9] == "X":
        if (int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + int(isbn[6]) * 4 + int(isbn[7]) * 3 + int(isbn[8]) * 2 + 10) % 11 == 0:
            return True
    else:
        return (int(isbn[0]) * 10 + int(isbn[1]) * 9 + int(isbn[2]) * 8 + int(isbn[3]) * 7 + int(isbn[4]) * 6 + int(isbn[5]) * 5 + int(isbn[6]) * 4 + int(isbn[7]) * 3 + int(isbn[8]) * 2 + int(isbn[9]) * 1) % 11 == 0
    return False 