# -*- coding: utf-8 -*-
from car import Car

my_new_car = Car('audi','a6',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()