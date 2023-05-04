import RPi.GPIO as io 
import time
from matplotlib import pyplot as pyp 

io.setmode(io.BCM)

leds=[21, 20, 16, 12, 7, 8, 25, 24]
io.setup(leds, io.OUT)

DAC = [26, 19, 13, 6, 5, 11, 9, 10]
io.setup(DAC, io.OUT, initial = 1)

comp = 4
troyka = 17
io.setup(troyka, io.OUT, initial = 0)
io.setup(comp, io.IN)

def dec2bin(n):
    return [int (i) for i in bin(n)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k +=2**i 
        io.output(DAC, dec2bin(k))
        time.sleep(0.005)
        if io.input(comp) == 0:
            k-=2**i
    return k

try:
    u = 0
    result = []
    time_start = time.time()
    count = 0

    print("Начало Заряда")
    while u < 256*0.95:    #256/4
        u = adc()
        result.append(u)
        #time.sleep(0)
        count += 1
        io.output(leds, dec2bin(u))
    io.setup(troyka, io.OUT, initial = 1)

    print("Начало Разряда")
    while u > 256*0.25:    #256*0.02
        u = adc()
        result.append(u)
        #time.sleep(0)
        count += 1
        io.output(leds, dec2bin(u))

    time_exp = time.time() - time_start

    print("Запись Данных")

    with open('data.txt', 'w') as f:
        for i in result:
            f.write(str(i)+'\n')


    with open('settings.txt', 'w') as f:
        f.write(str(1/time_exp/count)+'\n')
        f.write('0.01289')

    #print('General time {}, Time one exp {}, Middle freq of diskr, Step of kvant {}'.format(time_exp, time_exp/count, 1/time_exp/count, 0.013))

    print("Graphics")
    y = [i/256*3.3 for i in result]
    x = [i*time_exp/count for i in range(len(result))]
    pyp.plot(x, y)
    pyp.xlabel("Время")
    pyp.ylabel("Вольтаж")
    pyp.show()

finally:
    io.output(leds, 0)
    io.output(DAC, 0)
    io.cleanup()







