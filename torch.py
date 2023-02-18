#####################################################
#             Notification LED control              #
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
def torch_on():
    # IN 80% of android systems notification LED binded on red folder /sys/class/leds/red/brightness
    os.popen("echo 0 > /sys/class/leds/red/brightness")
    os.popen("echo 255 > /sys/class/leds/red/brightness")

def torch_off():
    os.popen("echo 0 > /sys/class/leds/red/brightness")

parser = argparse.ArgumentParser(description='Example: flashlight.py -on')

# добавляем аргументы командной строки
parser.add_argument('-on', '--on', action='store_true', help='Turning ON')
parser.add_argument('-off', '--off', action='store_true', help='Turning OFF')

# парсим аргументы командной строки
args = parser.parse_args()

# проверяем аргументы
if args.on:
    torch_on()
if args.off:
    torch_off()
else:
    print("Use -h for more info")