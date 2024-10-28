import smbus
import math
import matplotlib.pyplot as plt
import time

bus = smbus.SMBus(1)
list = []
try:
    while True:
        data = bus.read_byte_data(0x48, 0x40)
        V = 3.3 * float(data) / 255
        print(f"{len(list)+1}, Voltage: {V}V")
        if len(list) < 1000:
            list.append(V)
        if len(list) >= 1000:
            break
        time.sleep(0.005)
    plt.plot(list)
    plt.title('Voltage Trend')
    plt.ylabel('V')
    plt.xlabel('time')
    plt.show()
except KeyboardInterrupt:
    bus.close()