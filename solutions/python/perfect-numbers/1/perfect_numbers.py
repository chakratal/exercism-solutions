"""This function determines whether a given number is perfect, abundant, or deficient based on their aliquot sum."""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    for num in range(1, number):
        if number % num == 0:
            aliquot += num
    if aliquot == number:
        return "perfect"
    if aliquot > number:
        return "abundant"       
    return "deficient"