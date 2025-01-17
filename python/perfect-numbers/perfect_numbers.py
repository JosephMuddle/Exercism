def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        aliquot = sum([i for i in range(1, number//2+1) if number % i == 0])
        if aliquot == number:
            return "perfect"
        if aliquot > number:
            return "abundant"
        if aliquot < number:
            return "deficient"