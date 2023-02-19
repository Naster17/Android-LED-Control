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
![disco](https://user-images.githubusercontent.com/62520991/219944095-9db8b4f8-404c-45c9-8462-24944408894c.gif)


**Default method required ROOT**
