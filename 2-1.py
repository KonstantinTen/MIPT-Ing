import RPi.GPIO as io
import time
io.setmode(io.BCM)

LED = [21,20,16,12,7,8,25,24]
io.setup(LED, io.OUT)

for i in range(4):
    for i in range(8):
        io.output(LED[i], 1)
        time.sleep(0.2)
        io.output(LED[i], 0)

io.output(LED, 0)
io.cleanup()



