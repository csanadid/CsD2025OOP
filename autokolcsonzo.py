class Company:
    def __init__(self, name):
        self._name = name
        self._cars = []

    @property
    def name(self):
        return self._name
    
    @property
    def cars(self):
        for car in self._cars:
            print(f"Rendszámtábla: {car.licence_plate}, Ár: {car.price}, Típus: {car.type} Dátum: {car.date} Státusz: {car.is_leased}")

    @cars.setter
    def cars(self, new_car):
        self._cars.append(new_car)

    def lease_by_licence_plate (self, licence_plate):
        for car in self._cars:
            if car.licence_plate == licence_plate:
                return car.lease_car()
    
    def unlease_by_licence_plate (self, licence_plate):
        for car in self._cars:
            if car.licence_plate == licence_plate:
                return car.unlease_car()