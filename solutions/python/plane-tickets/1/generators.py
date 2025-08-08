"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ('A', 'B', 'C', 'D')
    for i in range(number):
        yield seats[i % len(seats)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    letter_gen = generate_seat_letters(number)
    seat_number = 1

    for i in range(1, number + 1):
        yield str(seat_number) + next(letter_gen)
        if i % 4 == 0:
            seat_number += 1 if seat_number + 1 != 13 else 2


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_gen = generate_seats(len(passengers))

    seated_passenger = {}
    for passenger in passengers:
        seated_passenger[passenger] = next(seat_gen)

    return seated_passenger

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for number in seat_numbers:
        code = str(number) + str(flight_id)
        for i in range(len(code), 12):
            code += '0'
        yield code