import smbus
import time

bus = smbus.SMBus(1)

try:
    while True:
        for data in range(0, 255):
            bus.write_byte_data(0x48, 0x42, data)
            time.sleep(0.01)
        for data in range(255, 0, -1):
            bus.write_byte_data(0x48, 0x42, data)
            time.sleep(0.01)
except KeyboardInterrupt:
    bus.write_byte_data(0x48, 0x42, 0)
    bus.close()