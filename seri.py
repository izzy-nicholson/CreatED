import serial, time  
import matplotlib.pyplot as plt
import numpy as np
port = "/dev/ttyACM1"  
baud = 115200  
s = serial.Serial(port)  
s.baudrate = baud

x_left_values = []
x_right_values = []
while True:  
    data = s.readline()
    print(data)
    tokens = data.decode('utf-8').split(", ")
    if (len(tokens) == 4):
        print(tokens)
        (name,x,y,z) = tokens
        if (name == 'Left'):
            x_left_values.append(x)
            x_l = np.array(x_left_values)
            plt.plot(x_l)
            plt.title('left')
            plt.show()
            plt.pause(0.0001)
            '''
        elif (name == 'Right'):
            x_right_values.append(x)
            x_r = np.array(x_right_values)
            plt.plot(x_r)
            plt.title('right')
            plt.show()'''
    time.sleep(0.1)
