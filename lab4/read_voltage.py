import smbus

bus = smbus.SMBus(1)

try:
    while True:
        data = bus.read_byte_data(0x48, 0x40)
        print(f"{data/255*3.3}V")
except KeyboardInterrupt:
    bus.close()