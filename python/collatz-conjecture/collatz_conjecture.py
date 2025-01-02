def steps(number):
    if number <= 0: 
        raise ValueError("Only positive integers are allowed")
    else:
        total = 0
        while number != 1:
            number = 3*number+1 if number % 2 else number // 2
            total += 1
        return total