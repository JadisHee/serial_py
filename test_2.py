
import serial
import time
import sys
import select

def setCom(port, buadrate):
    try:
        ser = serial.Serial(port, buadrate, timeout=1)
        print('串口连接成功')
        return ser
    except:
        print('串口连接失败')
        exit()


def send_data(data,ser):

    ser.write(data)
    print("发送数据: ", data.hex())

    while True:
        response = ser.readline().hex()
        if response:
            print("接收数据: ", response)
            break
        time.sleep(0.1)
    return response

if __name__ == '__main__':
    # 定义发送的报文
    send_imu = "77 04 00 59 5D"
    send_motor = "01 03 00 57 00 0C F4 1F"
    # 设置串口数据
    ser_imu = setCom('/dev/ttyUSB0',115200)
    ser_motor = setCom('/dev/ttyUSB1',9600)

    while True:
        # 执行通讯
        response_imu = send_data(send_imu,ser_imu)
        response_motor = send_data(send_motor, ser_motor)
        time.sleep(0.01)
        # 检测输入，当输入小写'q'时，退出程序
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = input()
            if line == 'q':
                break
    # 关闭串口
    ser_imu.close()
    ser_motor.close()
