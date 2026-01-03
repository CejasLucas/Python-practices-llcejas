list_cities = []
list_passengers = []

def run():
    print("\nWrite a program to process travel passenger data in a list ")
    print("of tuples with the format: [('name', DNI, destination)]")

    print("\nAlso, another list of tuples stores city names")
    print("and the country they belong to. Example: [('Buenos Aires', 'Argentina'), ...]")

    while True:
        print("\nWrite the corresponding number for said operation: ")
        print("(1) Add cities to the city list.")
        print("(2) Add passengers to the traveler list.")
        print("(3) Given a passenger's ID, display the city and country they are traveling to.")
        print("(4) Given a country, display how many passengers are traveling to that country.")
        print("(0) Exit the program.")
        number = int(input("Enter a number: "))
        levels = {
            1: add_city,
            2: add_passenger,
            3: search_by_dni,
            4: number_of_passengers_country
        }
        if number == 0:
            print("\nYou have finished the program")
            break
        elif number in levels:
            levels[number]()
        else:
            print("\nInvalid option, please re-enter a number")


def add_passenger():
    dni = int(input("\nEnter the passenger identification number: "))
    city = input("\nEnter the passenger's destination city: ")
    name = input("\nEnter the passenger's full name: ")
    passenger = (dni, city, name)
    list_passengers.append(passenger)


def add_city():
    city = input("\nEnter the name of the city: ")
    country = input("\nEnter the name of the country: ")
    city_country = (city, country)
    list_cities.append(city_country)


def search_by_dni():
    search_dni = int(input("\nEnter the identification number of the passenger to be searched for: "))
    index_passenger = passenger_dni_index(search_dni)
    if index_passenger is not None:
        dni, city, name = list_passengers[index_passenger]
        index_city = city_index(city)
        if index_city is not None:
            city_name, country = list_cities[index_city]
            print(f"{name} is traveling to {city_name}, {country}.")
        else:
            print(f"The passenger {name} exists but does not have a trip assigned.")
    else:
        print("Passenger not found.")


def number_of_passengers_country():
    search_country = input("\nEnter the name of the country: ").strip().lower()
    cities_in_country = [city for city, country in list_cities if country.lower() == search_country]

    if cities_in_country:
        number_of_passengers = 0
        for dni, destination, name in list_passengers:
            if destination in cities_in_country:
                number_of_passengers += 1
        print(f"\nThe number of passengers traveling to {search_country} is {number_of_passengers}")
    else:
        print("\nThe country sought was not found.")

def passenger_dni_index(search_dni):
    for i, passenger in enumerate(list_passengers):
        if search_dni == passenger[0]:
            return i
    return None


def city_index(search_city):
    for i, city_country in enumerate(list_cities):
        if search_city == city_country[0]:
            return i
    return None
