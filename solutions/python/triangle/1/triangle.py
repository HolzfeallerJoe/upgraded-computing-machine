def equilateral(sides):
    if check_if_triangle(sides):
        return len({*sides}) == 1
    return False


def isosceles(sides):
    if check_if_triangle(sides):
        return len({*sides}) <= 2
    return False


def scalene(sides):
    if check_if_triangle(sides):
        return len({*sides}) == 3
    return False


def check_if_triangle(sides):
    return (
        sides[0] + sides[1] >= sides[2]
        and sides[0] + sides[2] >= sides[1]
        and sides[1] + sides[2] >= sides[0]
        and not 0 in sides
    )