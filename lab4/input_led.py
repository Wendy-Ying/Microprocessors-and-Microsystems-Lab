import smbus

bus = smbus.SMBus(1)

try:
    while True:
        bright = int(input())
        if 0 < bright < 255:
            bus.write_byte_data(0x48, 0x42, bright)
except KeyboardInterrupt:
    bus.write_byte_data(0x48, 0x42, 0)
    bus.close()