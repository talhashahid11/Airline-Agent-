from agent import search_flights
from booking import book_flight

print("✈️ Airline Agent Started")

source = input("Enter departure city: ")
destination = input("Enter destination city: ")A

flights = search_flights(source, destination)

if not flights:
    print("No flights found")
else:
    print("\nAvailable Flights:")
    for i, f in enumerate(flights):
        print(f"{i+1}. {f['airline']} - ${f['price']}")

    choice = int(input("Select flight number: "))
    selected = flights[choice-1]

    print(book_flight(selected))
