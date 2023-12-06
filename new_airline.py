def get_travel_info():
    country = input("What is your destination?: ")
    month = input("Departing Month?: ")
    if month == "November" or month == "December" or month == "January":
        print("During the peak travel season, ticket prices will increase by 20%.")
    day = int(input("How many days?: "))
    return country, month, day


def get_passenger_info():
    num_person = int(input("How many passenger?: "))
    passenger_list = []
    for person in range(num_person):
        self = []
        print(f'Please enter passenger#{person + 1} info')
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        _class = input("Class: ")
        self.append(first_name)
        self.append(last_name)
        self.append(_class)
        passenger_list.append(self)
        print("********")
    return passenger_list


def check_high_season(month):
    if month == "November" or month == "December" or month == "January":
        return 1
    else:
        return 0


def get_travel_fee(country):
    for c in range(len(europe)):
        if country == europe[c]:
            return europe_distance[c]*10, 'Europe'
        elif country == asia[c]:
            return asia_distance[c]*10, 'Asia'


def get_hotel_fee(number_person, number_night):
    return number_person * number_night * 3000


europe = ["England", "Germany", "Italy", "France", "Belgium"]
europe_distance = [9435, 8672, 8705, 9390, 9097]
asia = ["China", "Japan", "Indonesia", "India", "Singapore"]
asia_distance = [3442, 4312, 2333, 4213, 2108]

# Main part
# Fill in code for main part below
in_country, in_month, in_day = get_travel_info()
passenger = get_passenger_info()
total = 0
total_fee = 0
hotel_cost = 0
for i in range(len(passenger)):
    firstname, lastname, f_class = passenger[i]
    fee, continent = get_travel_fee(in_country)

    if check_high_season(in_month) == 1:
        fee *= 1.2
    if f_class == 'Business':
        fee *= 1.5

    total_fee += fee
    hotel_cost = get_hotel_fee(len(passenger), in_day)
    total = total_fee + hotel_cost

    print(f"Passenger Name: {firstname} {lastname}")
    print(f"From Bangkok to {in_country} ({continent})")
    print(f"Traveling fee: {fee:.2f} Baht ({f_class})")
    print("********")

print(f"Hotel fee for {(len(passenger))} rooms x {in_day} nights is {hotel_cost:.2f} Baht")
print(f"The total cost is {total:.2f} Baht")
print("Enjoy your trip :)")
