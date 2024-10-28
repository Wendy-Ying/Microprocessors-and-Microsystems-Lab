import smbus
import matplotlib.pyplot as plt
import numpy as np
import time

# 初始化 I2C 总线
bus = smbus.SMBus(1)

# 初始化图形
plt.ion()  # 开启交互模式，实时更新图表
fig, ax = plt.subplots()
x_data = []
y_data = []
line, = ax.plot(x_data, y_data)

# 设置 x 和 y 轴标签
ax.set_xlabel("Time (s)")
ax.set_ylabel("Analog Input Value")

# 起始时间
start_time = time.time()

try:
    while True:
        # 读取 PCF8591 输入通道数据
        data = bus.read_byte_data(0x48, 0x40)  # 读取通道 0
        current_time = time.time() - start_time

        # 更新数据
        x_data.append(current_time)
        y_data.append(data)
        print(data)

        # 更新图表数据
        line.set_xdata(x_data)
        line.set_ydata(y_data)

        # 重新设置 x 轴和 y 轴范围
        ax.set_xlim(0, max(10, current_time))  # X 轴范围
        ax.set_ylim(0, 255)  # PCF8591 是 8 位 A/D，范围 0-255

        # 重新绘制图形
        plt.draw()
        plt.pause(0.01)  # 设置绘图间隔时间，避免 CPU 占用过高

except KeyboardInterrupt:
    bus.close()
    print("程序终止")

finally:
    plt.ioff()  # 关闭交互模式
    plt.show()  # 显示最终的静态图形
