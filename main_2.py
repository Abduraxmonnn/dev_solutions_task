# Project
from car import Car
from utilits.options import hello_options, type_options
from utilits.style import Bcolors

car_bmx_x6 = Car(brand_name="BMW", model_name="X6")


def main():
    print(Bcolors.OKBLUE + "----- Hello -----" + Bcolors.END)
    for key, value in hello_options.items():
        print(f"{Bcolors.UNDERLINE} {key} {Bcolors.END}", value)

    while True:

        input_option = int(input(f"Enter your option: "))

        match input_option:
            case 1:
                print(car_bmx_x6.car)
            case 2:
                for key, value in type_options(car_bmx_x6.color, car_bmx_x6.door, car_bmx_x6.engine,
                                               car_bmx_x6.wheel_diameter).items():
                    print(f"{Bcolors.BLUE} {key} {Bcolors.END}: {Bcolors.LIGHT_BLUE} {value} {Bcolors.END}\n")

                input_type_options = int(input("Enter your option: "))

                match input_type_options:
                    case 1:
                        print("Available colors: ", car_bmx_x6.available_colors())
                        new_color = int(input("Enter index of new color: "))
                        car_bmx_x6.color = car_bmx_x6.available_colors()[new_color]
                        print("-----/ Updated car detail /-----")
                        print(car_bmx_x6.car)
                    case 2:
                        print("Available doors: ", car_bmx_x6.available_doors())
                        new_door = int(input("Enter index of new door: "))
                        car_bmx_x6.door = car_bmx_x6.available_doors()[new_door]
                        print("-----/ Updated car detail /-----")
                        print(car_bmx_x6.car)
                    case 3:
                        new_engine = float(input("Enter new engine (for example: 3.2): "))
                        car_bmx_x6.engine = new_engine
                        print("-----/ Updated car detail /-----")
                        print(car_bmx_x6.car)
                    case 4:
                        new_wheel = int(input("Enter new wheel diameter (for example: 24): "))
                        car_bmx_x6.wheel_diameter = new_wheel
                        print("-----/ Updated car detail /-----")
                        print(car_bmx_x6.car)
            case 3:
                car_bmx_x6.move(duration=2)
            case 4:
                break


if __name__ == '__main__':
    main()
