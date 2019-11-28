# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

try:
    from combustion_car import CombustionCar
    from electric_car import ElectricCar

except ModuleNotFoundError:
    from public.electric_car import ElectricCar
    from public.combustion_car import CombustionCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__mode = CombustionCar

    def switch_to_combustion(self):
        self.__mode = CombustionCar

    def switch_to_electric(self):
        self.__mode = ElectricCar

    def get_remaining_range(self):
        entfernung = (CombustionCar.get_remaining_range(self) + \
                            ElectricCar.get_remaining_range(self))
        return entfernung

    def drive(self, dist):
        assert type(dist) == float
        mode = self.__mode 
        dist_mod1 = mode.get_remaining_range(self)
        if dist_mod1 > dist:
            mode.drive(self, dist)
        else:
            try:
                mode.drive(self, dist_mod1)
            except Warning:
                pass
            if mode == CombustionCar:
                self.switch_to_electric()
            elif mode == ElectricCar:
                self.switch_to_combustion()
            print(self.__mode)
            self.__mode.drive(self, dist-dist_mod1)



if __name__ == '__main__':
    h = HybridCar(40.0, 8.0, 25.0, 500.0)
    h.switch_to_combustion()
    h.drive(600.0) # depletes fuel, auto-switch
    print(h.get_gas_tank_status()) # (0.0, 40.0)
    print(h.get_battery_status()) # (20.0, 25.0)