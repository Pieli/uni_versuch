# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.
try:
    from public.car import Car
except ModuleNotFoundError:
    from car import Car

class CombustionCar(Car):
    # CombustionCar(Car) nicht vergessen
    def __init__(self, gas_capacity, gas_per_100km):
        if isinstance(gas_capacity, float) and gas_capacity >= 0:
            self.__gas_capacity = gas_capacity
            self.__gas_status = gas_capacity
        else:
            self.__gas_capacity = 0.0
            self.__gas_status = 0.0
            raise Warning('Wrong Type')
        if isinstance(gas_per_100km, float) and gas_per_100km >= 0:
            self.__gas_per_100km = gas_per_100km
        else:
            self.__gas_per_100km = 0.0
            raise Warning('Wrong Type') 

    def fuel(self, f):
        if isinstance(f, float):
            if self.__gas_status + f <= self.__gas_capacity:
                self.__gas_status += f
            else:
                raise Warning('Tank overfill')
        else:
            raise Warning('Input is not float')


    def get_gas_tank_status(self):
        return (self.__gas_status,self.__gas_capacity)

    def get_remaining_range(self):
        remaining = self.__gas_status / (self.__gas_per_100km/100)
        return remaining

    def drive(self, dist):
        assert type(dist) == float 
        pro_meile = self.__gas_per_100km/100
        self.__gas_status -= pro_meile*dist
        if self.__gas_status <= 0.0:
            raise Warning('Tank ist alle')

if __name__ == '__main__':
    c = CombustionCar(40.0, 8.0)
    entfernung = c.get_remaining_range()
    assert entfernung == 500
    c.drive(100.0) 
    assert c.get_gas_tank_status()[0]== 32.0
    entfernung = c.get_remaining_range()
    assert entfernung == 400.0
    c.fuel(5.0) 
    assert c.get_gas_tank_status()[0] == 37.0
