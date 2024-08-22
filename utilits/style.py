import time
import os


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_loading_bar(position, total_distance):
    bar_length = 40  # Adjust bar length as needed
    filled_blocks = int(position / total_distance * bar_length)
    empty_blocks = bar_length - filled_blocks
    loading_bar = "=" * filled_blocks + "🚗" + " " * empty_blocks
    print(f"\rLoading: [{loading_bar}] {position}/{total_distance}", end="")


def animate_car(target_time):
    clear_screen()
    position = 0
    max_width = 80  # Adjust max_width for different terminal sizes
    total_distance = max_width

    # Calculate sleep time based on target_time and total_distance
    sleep_time = target_time / total_distance

    # Calculate speed based on total_distance and target_time
    speed = total_distance / target_time

    while True:
        print_loading_bar(position, total_distance)
        time.sleep(sleep_time)
        clear_screen()
        position += 1
        if position > max_width:
            break
