import RPi.GPIO as io
import time
io.setmode(io.BCM)

dac = [26,19,13,6,5,11,9,10]
num = [1,0,1,0,1,0,1,0]

io.setup(dac, io.OUT)

io.output(dac, num)
time.sleep(8)


io.output(dac, 0)
io.cleanup()