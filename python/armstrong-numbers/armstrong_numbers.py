def is_armstrong_number(number):
    return (number == sum([int(i)**len(str(number)) for i in list(str(number))]))
