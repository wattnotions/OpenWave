import time
import digitalio
import board
import storage

print("Press button in next 5 seconds to enable CircuitPython file writing")


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


# setup the switch as before
switch = digitalio.DigitalInOut(board.BUTTON)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# wait 5 seconds to give the user a chance to press the button
for _ in range(50):
    if not switch.value:
        break
    time.sleep(0.1)



# then, check the switch and enable write access if needed
if not switch.value:
    storage.remount("/", False)
    print("rw flash enabled")
    led.value=1
else:
    print("rw flash disabled")
    led.value=0


