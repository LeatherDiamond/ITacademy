import datetime
import time

from data_models import DIGITS, SEPAR
from generators import colorizer, counter
from utils import print_time, screen_cleaner


def main():
    cntr = counter(5)
    color = colorizer(10)
    while True:
        current_digits = []
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        separator = SEPAR[next(cntr)]
        # '20:06:23'
        for i in range(0, 8):
            if current_time[i] == ':':
                current_digits.append(separator)
            else:
                current_digits.append(DIGITS[int(current_time[i])])
        clr = next(color)
        print_time(current_digits, clr)
        time.sleep(0.2)
        screen_cleaner()


if __name__ == "__main__":
    main()