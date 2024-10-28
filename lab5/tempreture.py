import smbus
import math
import matplotlib.pyplot as plt
import time

bus = smbus.SMBus(1)
list = []
try:
    while True:
        data = bus.read_byte_data(0x48, 0x40)
        Vr = 3.3 * float(data) / 255
        Rt = 10000 * Vr / (5 - Vr)
        T = 1 / (1/3950 * math.log(Rt/10000) + 1/273.15) - 273.15
        print(f"{len(list)+1}, Tempreture: {T}°C")
        if len(list) < 100:
            list.append(T)
        if len(list) >= 100:
            break
        time.sleep(0.1)
    plt.plot(list)
    plt.title('Tempreture Trend')
    plt.ylabel('T')
    plt.xlabel('time')
    plt.show()
except KeyboardInterrupt:
    bus.close()