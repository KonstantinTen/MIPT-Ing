import RPi.GPIO as io
import time
io.setmode(io.BCM)

LED = [21,20,16,12,7,8,25,24]
AUX = [22,23,27,18,15,14,3,2]

io.setup(LED, io.OUT)
io.setup(AUX, io.IN)

io.output(LED, 1)

try:
    while True:
        for i in range(8):
            io.output(LED[i], io.input(AUX[i]))
            time.sleep(0.1)
finally:
    io.output(LED, 0)
    io.cleanup()

