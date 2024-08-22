# Project
from car import Car

"""
Just demonstrated code.
"""

car_bmx_x6 = Car(brand_name="BMW", model_name="X6")
print('---------------/ Original Car /---------------\n', car_bmx_x6.car)

# Operations with Color
print('Current Color: ', car_bmx_x6.color)
print('Available Colors: ', car_bmx_x6.available_colors())
car_bmx_x6.color = 'White'  # You can not change color to not exists color.
print('\n\n---------------/ Data with updated color /---------------\n', car_bmx_x6.car)

# Other Operations
car_bmx_x6.engine = 3.2
car_bmx_x6.wheel_diameter = 24
car_bmx_x6.interior_material = 'Alcantara'
car_bmx_x6.fuel = 'Electro'
# print('Engine -', car_bmx_x6.engine)
# print('Wheel Diameter -', car_bmx_x6.wheel_diameter)
# print('Doors -', car_bmx_x6.doors)
# print('Fuel -', car_bmx_x6.fuel)
print('Available Doors:', car_bmx_x6.available_doors(is_dict=False))
car_bmx_x6.doors = 'Scissor'

print('\n\n---------------/ Updated Car: /---------------\n', car_bmx_x6.car)
