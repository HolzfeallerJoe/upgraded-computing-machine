def is_armstrong_number(number):
    power = len(str(number))
    rest = number
    total = 0

    while rest != 0:
        total += (rest % 10) ** power
        rest //= 10
    return total == number