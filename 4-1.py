import RPi.GPIO as io
import sys
io.setmode(io.BCM)

DAC = [26,19,13,6,5,11,9,10]
io.setup(DAC, io.OUT)

def dec2bin(a,n):
    return [int (i) for i in bin(a)[2:].zfill(n)]


try:
    while True:
        a = input("write 0-255\n")
        if a == "q":
            sys.exit()
        elif a.isdigit() and int(a)%1==0 and 0<=int(a)<=255:
            io.output(DAC, dec2bin(int(a),8))
            print("{:.4f}".format(int(a)*3.3/256))
        elif a.isdigit() and int(a)%1==0 and int(a)>255:
            print("write number only in 0-255\n")
        elif not a.isdigit():
            print("write only int number")

#except ValueError:
    #print("write number only in 0-255")

except KeyboardInterrupt:
    print("done")
finally:
    io.output(DAC, 0)
    io.cleanup()