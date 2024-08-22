# Project
from model import Model
from utilits.style import Bcolors, animate_car

db = []


class Car(Model):
    """
    Represents a car entity, providing a comprehensive description of its attributes.

    Attributes:
        brand_name (str): Inherited from Model, the name of the car brand.
        model_name (str): Inherited from Model, the name of the car model.
        _color (str, private): The car's exterior color.
        _door (str, private): The type of doors on the car.
        _engine (float, private): The engine displacement of the car in liters.
        _fuel (str, private): The primary fuel type used by the car.
        _interior_material (str, private): The material used for the car's interior upholstery.
        _wheel_diameter (int, private): The diameter of the car's wheels in inches.
        colors (dict, class): A dictionary containing available colors for different brands (populated externally).
        doors (dict, class): A dictionary containing available door types (populated externally).
    """

    def __init__(self, brand_name: str, model_name: str):
        """
        Initializes a new Car object.

        Args:
            brand_name (str): The name of the car brand.
            model_name (str): The name of the car model.
        """
        super().__init__(brand_name=brand_name, model_name=model_name)
        self._color = "BLACK"
        self._door = "SWAN"
        self._engine = 3.0
        self._fuel = "PETROL"
        self._interior_material = "LEATHER"
        self._wheel_diameter = 22

    # We can create class Colors and get 2 arguments car, cars and save to dict.
    colors = {
        "BMW": {
            1: "BLACK",
            2: "WHITE",
            3: "RED AND BLACK",
            4: "BLUE"
        },
        "LAMBORGHINI": {
            1: "BLACK",
            2: "ORANGE",
            3: "YELLOW",
            4: "CARBON"
        }
    }

    # We can create class Colors and get door and save to dict or list.
    doors = {
        1: "Swan",
        2: "Scissor",
        3: "Suicide",
        4: "Sliding",
        5: "Butterfly"
    }

    @property
    def car(self):
        """
        Returns a formatted string representation of the car's details.

        Returns:
            str: A formatted string containing car information.
        """
        data_format = {
            "id": len(db) + 1,
            "Brand name": self.brand,
            "Model name": self.model,
            "Color": self._color,
            "Fuel": self._fuel,
            "Interior material": self._interior_material,
            "Wheel diameter": self._wheel_diameter,
        }
        db.append(data_format)

        # Improved string formatting using f-strings for readability
        return f"{Bcolors.LIGHT_PURPLE}---> Car Parameters <---{Bcolors.END}\n\n" \
               f"Brand - {self.brand}\n" \
               f"Model - {self.model}\n" \
               f"Color - {self._color}\n" \
               f"Door - {self._door}\n" \
               f"Fuel - {self._fuel}\n" \
               f"Interior material - {self._interior_material}\n" \
               f"Wheel Diameter - {self._wheel_diameter}\n"

    @property
    def color(self):
        """
        Gets the current car color.

        Returns:
            str: The car's color.
        """
        return self._color

    @color.setter
    def color(self, color: str):
        """
        Sets the car's color, performing validation and providing informative messages.

        Args:
            color (str): The desired color for the car.

        Raises:
            ValueError: If the provided color is not available for the car's brand.
        """
        color = color.upper()
        if self.brand not in self.colors:
            print(f"{Bcolors.FAIL}Given color does not exist for {self.brand}!{Bcolors.END}")
            return

        if color not in self.colors[self.brand].values():
            print(f"{Bcolors.FAIL}Color '{color}' does not exist for {self.brand}{Bcolors.END}")
            return

        self._color = color
        print(f"{Bcolors.GREEN}Color changed successfully!{Bcolors.END}")

    @property
    def door(self):
        """
        Gets the current car door type.

        Returns:
            str: The car's door type.
        """
        return self._door

    @door.setter
    def door(self, door: str):
        """
        Sets the car's door type.

        Args:
            door (str): The desired door type for the car.
        """
        self._door = door.upper()

    @property
    def engine(self):
        """
        Gets the current car engine displacement.

        Returns:
            float: The car's engine displacement.
        """
        return self._engine

    @engine.setter
    def engine(self, engine: float):
        """
        Sets the car's engine displacement.

        Args:
            engine (float): The desired engine displacement for the car.
        """
        self._engine = engine

    @property
    def fuel(self):
        """
        Gets the current car fuel type.

        Returns:
            str: The car's fuel type.
        """
        return self._fuel

    @fuel.setter
    def fuel(self, fuel: str):
        """
        Sets the car's fuel type.

        Args:
            fuel (str): The desired fuel type for the car.
        """
        self._fuel = fuel.upper()

    @property
    def interior_material(self):
        """
        Gets the current car interior material.

        Returns:
            str: The car's interior material.
        """
        return self._interior_material

    @interior_material.setter
    def interior_material(self, interior_material: str):
        """
        Sets the car's interior material.

        Args:
            interior_material (str): The desired interior material for the car.
        """
        self._interior_material = interior_material.upper()

    @property
    def wheel_diameter(self):
        """
        Gets the current car wheel diameter.

        Returns:
            int: The car's wheel diameter.
        """
        return self._wheel_diameter

    @wheel_diameter.setter
    def wheel_diameter(self, wheel_diameter: int):
        """
        Sets the car's wheel diameter.

        Args:
            wheel_diameter (int): The desired wheel diameter for the car.
        """
        self._wheel_diameter = wheel_diameter

    def available_colors(self, is_dict: bool = True):
        """
        Returns a list or dictionary of available colors for the car's brand.

        Args:
            is_dict (bool, optional): Whether to return a dictionary or a list. Defaults to True.

        Returns:
            Union[dict, list]: A dictionary or a list of available colors.
        """
        if is_dict:
            return self.colors[self.brand.upper()]
        else:
            return list(self.colors[self.brand.upper()].values())

    def available_doors(self, is_dict: bool = True):
        """
        Returns a list or dictionary of available door types.

        Args:
            is_dict (bool, optional): Whether to return a dictionary or a list. Defaults to True.

        Returns:
            Union[dict, list]: A dictionary or a list of available door types.
        """
        if is_dict:
            return self.doors
        else:
            return list(self.doors.values())

    def move(self, duration: int = 5):
        animate_car(duration)
