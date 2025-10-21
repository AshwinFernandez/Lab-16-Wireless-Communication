from machine import Pin
import time

# Define input pins individually
input16 = Pin(16, Pin.IN, Pin.PULL_DOWN)
input17 = Pin(17, Pin.IN, Pin.PULL_DOWN)
input18 = Pin(18, Pin.IN, Pin.PULL_DOWN)
input19 = Pin(19, Pin.IN, Pin.PULL_DOWN)

# Define output pins individually
output12 = Pin(12, Pin.OUT)
output13 = Pin(13, Pin.OUT)
output14 = Pin(14, Pin.OUT)
output15 = Pin(15, Pin.OUT)

# Make sure all outputs start LOW
output12.value(0)
output13.value(0)
output14.value(0)
output15.value(0)

while True:
    # --- Handle input pin 16 ---
    if input16.value() == 1:
        output12.value(1)
    else:
        output12.value(0)

    # --- Handle input pin 17 ---
    if input17.value() == 1:
        output13.value(1)
    else:
        output13.value(0)

    # --- Handle input pin 18 ---
    if input18.value() == 1:
        output14.value(1)
    else:
        output14.value(0)

    # --- Handle input pin 19 ---
    if input19.value() == 1:
        output15.value(1)
    else:
        output15.value(0)

    # Small delay to prevent unnecessary CPU load
    time.sleep(0.05)
