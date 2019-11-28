from unittest import TestCase
from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar
from public.hybrid_car import HybridCar


class TestCars(TestCase):
    def setUp(self):
        self.c = CombustionCar(40.0, 8.0)
        self.e = ElectricCar(25.0, 500.0)

    def test_comb_remaining_range(self):
        self.assertAlmostEqual(500.0, self.c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        self.c.drive(25.0)
        self.assertAlmostEqual(38.0, self.c.get_gas_tank_status()[0], delta=0.001)
    
    def test_comb_fuel(self):
        bla = self.c
        bla.drive(25.0)
        bla.fuel(1.0)
        self.assertEqual(39.0, bla.get_gas_tank_status()[0])

    def test_comb_tank_status(self):
        pass

    def test_comb_range(self):
        pass



#####ELEKTRO#######
   
    def test_elec_remaining_range(self):
        self.assertAlmostEqual(500.0, self.e.get_remaining_range(), delta=0.001)
        

    def test_elec_drive(self):
        self.e.drive(100.0)
        self.assertAlmostEqual(20.0, self.e.get_battery_status()[0], delta=0.001)
        
        with self.assertRaises(Warning):
            self.e.drive(600.0)

    def test_elec_charge(self):
        self.e.drive(100.0)
        self.e.charge(5.0)
        self.assertAlmostEqual(25.0, self.e.get_battery_status()[0], delta=0.001)

        with self.assertRaises(Warning):
            self.e.charge(25.0)
