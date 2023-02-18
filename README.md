# Android LED-Controler [Python] 

## About:
It was made as simple and clear as possible without superfluous. So that everyone can understand how it works!

## DEMO:
Video Soon!

**Example code to enable and disable phone flashlight:**
```python
import os

def flashlight_on():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")
    os.popen("echo 255 > /sys/class/leds/flashlight/brightness")

def flashlight_off():
    os.popen("echo 0 > /sys/class/leds/flashlight/brightness")
    
```
