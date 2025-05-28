from auto import Car

class Teherauto (Car):
    def __init__(self, licence_plate, type, date, price):
        super().__init__(licence_plate, type, date, price)
        self._extras = ["minivan", "8_passengers" "removeable_seats_for_more_room"]

    @property
    def licence_plate(self):
        return self._licence_plate
    
    @property
    def type(self):
        return self._type
    
    @property
    def date(self):
        return self._date
    
    @property
    def price(self):
        return self._price
       
    @property
    def is_leased(self):
        return self._is_leased
    
    def lease_car(self):
        if not self._is_leased:
            self._is_leased = True
        else:
            print("Ez az autó már foglalt")

    def unlease_car(self):
        if self._is_leased:
            self._is_leased = False
        else:
            print("Ez az autó még nem foglalt")