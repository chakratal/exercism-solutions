
'''This function determines if a number is an Armstrong number or not. An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.'''


def is_armstrong_number(number):
    length = len(str(number))
    total = 0

    for num in str(number):
        total += int(num)**length
    return total == number