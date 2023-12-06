import sys

CITY_AIRPORT_CODES = {'Don Mueang': 'DMK', 'Chiang Mai': 'CNX',
                      'Chiang Rai': 'CEI', 'Phitsanulok': 'PHS',
                      'Khon Kaen': 'KKC', 'Udon Thani': 'UTH',
                      'Ubon Ratchathani': 'UBP', 'Phuket': 'HKT',
                      'Hat Yai': 'HDY', 'Surat Thani': 'URT', 'Krabi': 'KBV'
                      }

AIRPORT_CODES = ['DMK', 'CNX', 'CEI', 'PHS', 'KKC', 'UTH', 'UBP', 'HKT',
                 'HDY', 'URT', 'KBV'
                 ]

TICKET_PRICES = {'DMK': {'CNX': 1630, 'CEI': 1230, 'PHS': 1040, 'KKC': 1080,
                         'UTH': 1260, 'UBP': 1130, 'HKT': 1650, 'HDY': 1520,
                         'URT': 1150, 'KBV': 990
                         },
                 'CNX': {'DMK': 1630, 'KKC': 1250, 'HKT': 2180, 'HDY': 1870,
                         'URT': 1620, 'KBV': 1860},
                 'CEI': {'DMK': 1230},
                 'PHS': {'DMK': 1040},
                 'KKC': {'DMK': 1080, 'CNX': 1250, 'HKT': 1600},
                 'UTH': {'DMK': 1260, 'HKT': 2620},
                 'UBP': {'DMK': 1130},
                 'HKT': {'DMK': 1650, 'CNX': 2180, 'KKC': 1600, 'UTH': 2620,
                         'HDY': 2090},
                 'HDY': {'DMK': 1520, 'CNX': 1870, 'HKT': 2090},
                 'URT': {'DMK': 1150, 'CNX': 1620},
                 'KBV': {'DMK': 990, 'CNX': 1860}
                 }


def find_airport_code():
    """ Read city name from user input.
        If user enters invalid city name, keep asking user to input
        another city name.
        If city name is valid, display the airport code.
    """
    while True:
        input_city = input("Enter city or Done: ")
        if input_city == 'Done':  # ext the function when input is 'done'
            break
        # when the input city is wrong or not available in choice
        if CITY_AIRPORT_CODES.get(input_city) is None:
            print(f'Airport code of {input_city} is not available')
            print("Available airports:")
            print("Don Mueang / Chiang Mai / Chiang Rai / Phitsanulok /")
            print("Khon Kaen / Udon Thani / Ubon Ratchathani /")
            print("Phuket / Hat Yai/ Surat Thani / Krabi")
            continue
        else:
            print(f"Airport code of {input_city} is {CITY_AIRPORT_CODES.get(input_city)}")


def read_airport_code(msg):
    """ Receive msg string as function parameter. This string msg to show
        user what to input.
        If user enters invalid airport code, keep asking user to input another
        airport code.
        If airport code is valid, return such airport code.
    """
    while True:
        code = input(f"{msg}")
        if code in AIRPORT_CODES:  # check if the input code is available in provided city code
            return code


def get_flight_info_str(direct, origin, destination, price):
    """ From the information of flight (direct or not, origin and destination
        airport codes, and flight price),
        Return the string contain flight information

        :param direct: boolean
        :param origin:  string
        :param destination: string
        :param price:  int
        :return: total payment based on the customer's choices
        where each room fee costs 2500 Baht per day.
        >>> get_flight_info_str(True, 'DMK', 'HKT', 1650)
        'DMK-HKT: 1650.00 Baht'
        >>> get_flight_info_str(True, 'HKT', 'KKC', 1600)
        'HKT-KKC: 1600.00 Baht'
        >>> get_flight_info_str(False, 'CEI', 'HKT', 2880)
        'CEI-DMK-HKT: 2880.00 Baht'
        >>> get_flight_info_str(False, 'PHS', 'UBP', 2170)
        'PHS-DMK-UBP: 2170.00 Baht'
    """
    if direct is True:
        return f'{origin}-{destination}: {price:.2f} Baht'
    else:
        return f'{origin}-DMK-{destination}: {price:.2f} Baht'


def find_direct_flights_under_budget():
    """ Read budget value and origin from user inputs.
        Report direct flights with price below the budget, starting from origin.
        If there is no direct flight, report None.
    """
    while True:
        budget = int(input("Enter your budget: "))
        origin = input("Enter origin airport code: ")

        while origin not in AIRPORT_CODES:  # make user input the origin code until the input available code
            origin = input("Enter origin airport code: ")

        available_flights = []

        for destination, price in TICKET_PRICES[origin].items():
            if price <= budget:  # add all the destination city and their prices that under the provided budget
                available_flights.append((CITY_AIRPORT_CODES[destination], price))

        if available_flights:
            print(f"Available direct flights from {origin}:")
            for destination, price in available_flights:  # print all available flights
                print(f"{origin}-{destination}: {price:.2f} Baht")
        else:
            print("None")


def find_direct_flight_price(origin, destination):
    """ From the given origin and dst, return the price of direct flight
        from source to dst. If there is no direct flight available, return zero.

        :param origin: string
        :param destination: string
        :return: price if direct flight between origin and dst exists.
        Otherwise, return zero.
        >>> find_direct_flight_price('DMK', 'HKT')
        1650
        >>> find_direct_flight_price('CNX', 'KBV')
        1860
        >>> find_direct_flight_price('CEI', 'KKC')
        0
        >>> find_direct_flight_price('HDY', 'URT')
        0
    """
    return TICKET_PRICES[origin].get(destination, 0)


def find_connecting_flight_price(origin, destination):
    """ Given origin and dst, find price of connecting flight from origin to
        DMK and from DMK to destination.

        In addition, let the connecting point be DMK only.  This airline only
        operates connecting flights that stop at DMK.

        If either origin or destination is DMK, it will return price of
        direct flight.

        If both origin and destination are the same, return zero.

        :param origin: string
        :param destination: string
        :return: price of connecting flight between origin and destination,
        where (1) the first direct flight in this connecting flight is from
        origin to DMK, and
              (2) the second direct flight is from DMK to destination.
        >>> find_connecting_flight_price('CEI', 'HKT')
        2880
        >>> find_connecting_flight_price('PHS', 'UBP')
        2170
        >>> find_connecting_flight_price('UTH', 'URT')
        2410
        >>> find_connecting_flight_price('KBV', 'CEI')
        2220
        >>> find_connecting_flight_price('CNX', 'CNX')
        0
        >>> find_connecting_flight_price('DMK', 'CEI')
        1230
        >>> find_connecting_flight_price('KBV', 'DMK')
        990
    """
    if destination == origin:  # check if destination is the same as the origin
        price = 0
        return price
    elif origin == 'DMK' or destination == 'DMK':  # check if destination or origin is DMK
        price = TICKET_PRICES[origin].get(destination)
        return price
    else:
        price = TICKET_PRICES[origin].get('DMK') + TICKET_PRICES['DMK'].get(destination)
        return price


def find_flight_price():
    """ Read origin and destination from user inputs.
        If direct flight exists, report price of direct flight.
        Otherwise, find and report price of connecting flight.
    """
    while True:
        origin = input("Enter origin: ")
        while origin not in AIRPORT_CODES:
            origin = input("Enter origin: ")

        destination = input("Enter destination: ")
        while destination not in AIRPORT_CODES:
            destination = input("Enter destination: ")

        if origin == destination:
            print("Origin and destination cannot be the same.")
            continue

        price = find_connecting_flight_price(origin, destination)

        if origin == 'DMK' or destination == 'DMK':  # check if destination or origin is DMK
            print(f"Direct flight: {origin}-{destination}: {price:.2f} Baht")
            break
        else:  # if not provide the connecting flight, transfer  at DMK
            print(f"No direct flight between {origin}-{destination}")
            print(f"Connecting flight: {origin}-DMK-{destination}: {price:.2f} Baht")
            break


def find_all_flights_from_origin():
    """ Read origin from user input.
        First, report information of direct flights, starting from origin.
        Then, report information of connecting flights, starting from origin.
    """
    while True:
        origin = input("Enter origin: ")
        while origin not in AIRPORT_CODES:
            origin = input("Enter origin: ")

        direct_flights = []
        connecting_flights = []

        for destination, price in TICKET_PRICES[origin].items():
            if price > 0:
                direct_flights.append((f"{origin}-{destination}", price))
            else:
                connecting_price = find_connecting_flight_price(origin, destination)
                connecting_flights.append((f"{origin}-DMK-{destination}", connecting_price))

        print("Direct flights:")
        if len(direct_flights) != 0:
            for flight, price in direct_flights:
                print(f"{flight}: {price:.2f} Baht")
        elif len(direct_flights) == 0:
            print("None")

        print("Connecting flights:")
        if len(connecting_flights) != 0:
            for flight, price in connecting_flights:
                print(f"{flight}: {price:.2f} Baht")
        elif len(connecting_flights) == 0:
            print("None")
        break


def find_available_flight_info(origin, destination):
    """ Given origin and dst, find price of available flight from origin to
        destination.
        If direct flight is available, return the price of such direct flight.
        Otherwise, use connecting flight.
        Return 2 values that are (1) corresponding flight string (from
        function get_flight_str) and (2) price of the flight

        :param origin: string
        :param destination: string
        :return: flight string and price of the flight from origin to
        destination.

        >>> find_available_flight_info('CEI', 'HKT')
        ('CEI-DMK-HKT: 2880.00 Baht', 2880)
        >>> find_available_flight_info('PHS', 'UBP')
        ('PHS-DMK-UBP: 2170.00 Baht', 2170)
        >>> find_available_flight_info('UTH', 'DMK')
        ('UTH-DMK: 1260.00 Baht', 1260)
        >>> find_available_flight_info('KBV', 'CEI')
        ('KBV-DMK-CEI: 2220.00 Baht', 2220)
    """
    if origin == destination:
        return '', 0
    # Direct flight is available
    direct_flight_price = TICKET_PRICES.get(origin, {}).get(destination, None)
    if direct_flight_price is not None:
        flight_string = f"{origin}-{destination}: {direct_flight_price:.2f} Baht"
        return flight_string, direct_flight_price

    # No direct flight, use connecting flight
    connecting_price = find_connecting_flight_price(origin, destination)
    flight_string = f"{origin}-DMK-{destination}: {connecting_price:.2f} Baht"
    return flight_string, connecting_price


def reserve_ticket(_booking_list):
    """ Receive _booking list as function parameter.
        Note that _booking_list is a list of booking dictionaries.
        Each dictionary has 7 keys: first name, last name, origin, destination,
        flight info (which is flight string), price, and status.
        The status for ticket reservation is always 'Waiting'

        Read origin, destination, first name, last name from user inputs.
        Find available flight price from origin to destination.
        Add dictionary of booking items into a _booking list.
    """
    while True:
        origin = input("Enter origin: ")
        while origin not in AIRPORT_CODES:  # make user input the origin code until the input available code
            origin = input("Enter origin: ")

        destination = input("Enter destination: ")
        while destination not in AIRPORT_CODES:  # make user input the destination code until the input available code
            destination = input("Enter destination: ")
        if origin == destination:
            print("Origin and destination cannot be the same. Try again.")
            break
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")

        flight_price = find_connecting_flight_price(origin, destination)

        if flight_price is not None:  # if flight is available, add the provided information in list
            booking = {
                "firstname": first_name,
                "lastname": last_name,
                "origin": origin,
                "destination": destination,
                "flight info": f"{origin}-{destination}",
                "price": f"{flight_price:.2f} Baht",
                "status": "Waiting"
            }
            # Add the booking to the list
            booking_list.append(booking)

            # Print the booking details
            print(f"{first_name} {last_name}: {origin}-{destination}: {flight_price:.2f} Baht, Status: Waiting")
            break


def display_booking_list(_booking_list):
    """ Display information of _booking_list
    """
    for booking in booking_list:
        first_name = booking["firstname"]
        last_name = booking["lastname"]
        flight_info = booking["flight info"]
        price = booking["price"]
        status = booking["status"]

        print(f"{first_name} {last_name}: {flight_info}: {price}, Status: {status}")


def change_booking_status(_booking_list):
    """ Receive _booking list as function parameter.
        Read first name and last name from user inputs.
        In addition, ask user for new status to update: Confirmed (or CF) or
        Canceled (CC)
        If ticket under the given first name and last name is found in the
        _booking_list, change status of that ticket.
        If ticket under the given first name and last name is not found in the
        _booking_list, notify user.
    """
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    choice = ['CF', 'CC', 'CONFIRM', 'CANCEL']

    # Check if the provided status is valid
    while True:
        status = input("Do you want to confirm or cancel booking (CF/CC)? ")
        if status not in choice:
            status = input("Do you want to confirm or cancel booking (CF/CC)? ")

        # Find the booking with matching first name and last name
        for booking in booking_list:
            if booking.get("firstname") == first_name and booking.get("lastname") == last_name:
                if status in ['CF', 'CONFIRM']:
                    booking["status"] = "Confirmed"
                else:
                    booking["status"] = "Canceled"
                print(f"{first_name} {last_name}: {booking['flight info']}: {booking['price']}, "
                      f"Status: {booking['status']}")
            else:
                print("Invalid first name or last name. Please try again.")
        break


def run_choice(_choice, _booking_list):
    """ Receive menu choice (_choice) and booking_list as function parameters.
        Call function corresponding to each choice.
    """
    if _choice == 1:
        find_airport_code()
    elif _choice == 2:
        find_direct_flights_under_budget()
    elif _choice == 3:
        find_flight_price()
    elif _choice == 4:
        find_all_flights_from_origin()
    elif _choice == 5:
        reserve_ticket(_booking_list)
    elif _choice == 6:
        display_booking_list(_booking_list)
    elif _choice == 7:
        change_booking_status(_booking_list)


def read_choice():
    """ Reade menu choice (_choice) as user input.
        If user enters invalid menu choice, keep asking user to enter
        another menu choice.
        Once the menu choice is valid, return such menu choice.
    """

    # The following partial code is given.
    # Feel free to use it to show the choice menu.
    choice_lst = [0, 1, 2, 3, 4, 5, 6, 7]
    while True:
        print('\nChoices')
        print('1. Find airport code')
        print('2. Find direct flights under budget')
        print('3. Find price')
        print('4. Find all flights from origin')
        print('5. Reserve ticket')
        print('6. Display booking list')
        print('7. Change booking status')
        print('0. Exit')
        _booking_list = []
        _choice = int(input("Enter your choice: "))
        if _choice == 0:
            sys.exit()
        elif _choice in choice_lst:
            run_choice(_choice, _booking_list)
            continue
        else:
            print("Your choice is invalid. Choose again.")
            continue


# Main
booking_list = []
# Fill the remaining main part
read_choice()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest

    doctest.testmod()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
