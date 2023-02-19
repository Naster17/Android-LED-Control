# Android LED-Controler [Python] 

## About:
It was made as simple and clear as possible without superfluous. So that everyone can understand how it works!


**Example code to enable and disable phone flashlight:**
```python
import os

def flashlight_on():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")
    os.popen("echo 255 > /sys/class/leds/flashlight/brightness")

def flashlight_off():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")
    
```

## DEMO:
![disco](https://user-images.githubusercontent.com/62520991/219944210-a9112467-1b03-4240-8ea4-745d5b1d6909.gif)


**Default method required ROOT**
