from flight_api import get_flights

def search_flights(source, destination):
    flights = get_flights()
    return [f for f in flights if f["from"].lower() == source.lower() and f["to"].lower() == destination.lower()]
