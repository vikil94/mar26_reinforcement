class Location:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

class Trip:

    destinations = []

    def add_location(self, destination):
        self.destinations.append(destination)

    def trip_show(self):
        print("Begin Trip")
        for i in range(0, len(self.destinations)):
             print(f"Travelled from {self.destinations[i - 1]} to {self.destinations[i]}")
             print("Get outta here")



loc1 = Location("Toronto")
loc2 = Location("Ottawa")

trip = Trip()
trip.add_location(loc1)
trip.add_location(loc2)

print(trip.trip_show())
