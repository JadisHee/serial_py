import serial
import time
import sys
import select



# 串口配置
try:
    ser = serial.Serial('/dev/ttyUSB4', 115200, timeout=1)
    print('串口连接成功')
except:
    print('串口连接失败')
    exit()
    

# 发送数据
def send_data(data):

    ser.write(data)
    print("发送数据: ", data.hex())

    while True:
        response = ser.readline().hex()
        if response:
            print("接收数据: ", response)
            break
        time.sleep(0.1)



# 主函数
if __name__ == '__main__':

    data = "77 04 00 59 5D"
    # 发送数据并等待接收回复
    while True:
        send_data(data)
        time.sleep(1)
        # 检测输入，当输入小写'q'时，退出程序
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = input()
            if line == 'q':
                break
    
    ser.close()
