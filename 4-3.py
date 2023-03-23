import RPi.GPIO as io
#import sys
#import time
io.setmode(io.BCM)
io.setup(2, io.OUT)

DAC = [26,19,13,6,5,11,9,10]
io.setup(DAC, io.OUT)

pwm=io.PWM(2,1000)
pwm.start(0)

try:
    while True:
        duty_cycle = int(input())
        pwm.ChangeDutyCycle(duty_cycle)
        print("{:.2f}".format(duty_cycle*3.3/100))

finally:
    io.output(2,0)
    io.output(DAC, 0)
    io.cleanup()