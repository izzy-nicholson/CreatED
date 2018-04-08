import serial, time  
import matplotlib.pyplot as plt
import numpy as np
port = "/dev/ttyACM0"  
baud = 115200  
s = serial.Serial(port)  
s.baudrate = baud

left_values = []
right_values = []

start = time.time()
print(start)
while (time.time() - start < 30):  
    data = s.readline()
    #print(data)
    tokens = data.decode('utf-8').split(", ")
    if (len(tokens) == 4):
       # print(tokens)
        (name,x,y,z) = tokens
        if (name == 'Left'):
            left_values.append(','.join([x,y,z]))
        elif (name == 'Right'):
            right_values.append(','.join([x,y,z]))

with open('left', 'w') as f:
    for i in left_values:
        f.write(i)
        f.write('\n')

with open('right', 'w') as f:
    for i in right_values:
        f.write(i)
        f.write('\n')
