import RPi.GPIO as io
import time
io.setmode(io.BCM)
io.setup(14, io.OUT)
io.setup(15, io.IN)

time.sleep(1)
io.output(14, io.input(15))
time.sleep(4)

io.cleanup()



