# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
try:
    from public.car import Car
except ModuleNotFoundError:
    from car import Car

class ElectricCar:

    def __init__(self, battery_size, battery_range_km):
        if isinstance(battery_size, float) and battery_size >= 0:
            self.__size = battery_size
            self.__status = battery_size
        else:
            self.__size = 0.0
            self.__status = 0.0
            raise Warning('Wrong Type')
        if isinstance(battery_range_km, float) and battery_range_km >= 0:
            self.__range_km = battery_range_km
        else:
            self.__range_km = 0.0
            raise Warning('Wrong Type')

    def charge(self, kwh):
        assert isinstance(kwh, float)
        status_new = self.__status + kwh
        if  status_new <= self.__size:
                self.__status = status_new
        else:
            raise Warning('Battery overcharged')

    def get_battery_status(self):
        actual = self.__status
        size = self.__size
        return(actual , size)

    def get_remaining_range(self):
        rate = self.__size/self.__range_km
        return self.__status/rate

    def drive(self, dist):
        assert isinstance(dist, float)
        rate = self.__size/self.__range_km
        self.__status -= rate*dist
        if self.__status <= 0.0:
            raise Warning('Battery ist alle')

if __name__ == '__main__':
    """
    c = ElectricCar(25, )
    entfernung = c.get_remaining_range()
    assert entfernung == 500
    c.drive(100.0) 
    assert c.get_gas_tank_status()[0]== 32.0
    entfernung = c.get_remaining_range()
    assert entfernung == 400.0
    c.fuel(5.0) 
    assert c.get_gas_tank_status()[0] == 37.0
    """