import smbus

bus = smbus.SMBus(1)

try:
    while True:
        data = bus.read_byte_data(0x48, 0x40)
        bus.write_byte_data(0x48, 0x42, data)
        print(data)
except KeyboardInterrupt:
    bus.write_byte_data(0x48, 0x42, 0)
    bus.close()