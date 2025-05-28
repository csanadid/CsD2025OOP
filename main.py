from autokolcsonzo import Company
from szemelyauto import Szemelyauto
from teherauto import Teherauto

class LeasingSystem:

    def __init__(self):
        self._company = Company("BP Autó KFT")
        self._init_data()

    def _init_data(self):
        self._company.cars = Szemelyauto("ABC-123", "Toyota", "2025-07-01", 12000)
        self._company.cars = Szemelyauto("DEF-456", "Toyota", "2025-07-01", 12000)
        self._company.cars = Teherauto("KFC-563", "Mercedes", "2025-07-01", 20000)

    def user_interact(self):
        while True:
            print("1. Autók listája")
            print("2. Autó bérlése")
            print("3. Bérlés lemondása")
            print("4. Kilépés")

            menu = input("Menüpont kiválasztása: ")

            if menu == "1":
                self._company.cars
            elif menu == "2":
                license_plate = input("Adja meg a rendszámot: ")
                self._company.lease_by_licence_plate(license_plate)
            elif menu == "3":
                license_plate = input("Adja meg a rendszámot: ")
                self._company.unlease_by_licence_plate(license_plate)
            elif menu == "4":
                break


leasing_system = LeasingSystem()
leasing_system.user_interact()
