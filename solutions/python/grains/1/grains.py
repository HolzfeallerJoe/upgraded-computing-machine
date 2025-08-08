def square(number):
    if  number <= 0 or number > 64:
        raise ValueError('square must be between 1 and 64')
    grains = 1
    for _ in range(1, number):
       grains = (grains * 2)
    return grains


def total():
    return sum(square(i) for i in range(1, 64 + 1))
