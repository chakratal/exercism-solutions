"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    seat_generator = (["A", "B", "C", "D"])

    for num in range(number):
        if num % 4 == 0:
            yield seat_generator[0]
        elif num % 4 == 1:
            yield seat_generator[1]
        elif num % 4 == 2:
            yield seat_generator[2]
        else:
            yield seat_generator[3]
        
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

    seat_generator = (["A", "B", "C", "D"])
    
    for num in range(number):
        row = num // 4 + 1
        if row >= 13:
            row = num // 4 + 2
            if num % 4 == 0:
                yield str(row) + seat_generator[0]
            elif num % 4 == 1:
                yield str(row) + seat_generator[1]
            elif num % 4 == 2:
                yield str(row) + seat_generator[2]
            else:
                yield str(row) + seat_generator[3]          
        elif num % 4 == 0:
            yield str(row) + seat_generator[0]
        elif num % 4 == 1:
            yield str(row) + seat_generator[1]
        elif num % 4 == 2:
            yield str(row) + seat_generator[2]
        else:
            yield str(row) + seat_generator[3]

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat = generate_seats(len(passengers))
    assignments = {}

    for passenger in passengers:
        assignments[passenger] = next(seat)
    return assignments

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        zeros = 12 - (len(seat) + len(flight_id))
        yield seat+flight_id+("0"*zeros)
    