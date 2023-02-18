#####################################################
#             Flashlight control                    #
#                                                   #
# Conducted testing for Redmi Note 9 Pro Android 10 #
# By changing the data in the LED brightness file,  #
#           it can be turned on or off.             # 
#                                                   #
# You can also check for yourself all the available #
#       LEDs are available along the way:           #
#               /sys/class/leds/                    #
#####################################################

import os
import argparse

def flashlight_on():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")
    os.popen("echo 255 > /sys/class/leds/flashlight/brightness")

def flashlight_off():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")



# создаем объект парсера
parser = argparse.ArgumentParser(description='Example: flashlight.py -on')

# добавляем аргументы командной строки
parser.add_argument('-on', '--on', action='store_true', help='Turning ON')
parser.add_argument('-off', '--off', action='store_true', help='Turning OFF')

# парсим аргументы командной строки
args = parser.parse_args()

# проверяем аргументы
if args.on:
    flashlight_on()
if args.off:
    flashlight_off()
else:
    print("Use -h for more info")