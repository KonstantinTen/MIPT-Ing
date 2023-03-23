import RPi.GPIO as io
import time
io.setmode(io.BCM)

DAC = [26,19,13,6,5,11,9,10]
io.setup(DAC, io.OUT)

def dec2bin(a,n):
    return [int (i) for i in bin(a)[2:].zfill(n)]


try:
    a = input("write 0-255\n")
    while True:
        if not a.isdigit():
            print("write correct value")
        t = int(a)/512
        for i in range(256):
            io.output(DAC, dec2bin(i,8))
            time.sleep(t)
        for i in range(255,-1,-1):
            io.output(DAC,dec2bin(i,8))
            time.sleep(t)

finally:
    io.output(DAC, 0)
    io.cleanup()