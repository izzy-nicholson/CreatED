import matplotlib.pyplot as plt
import numpy as np
import math

tiny = 0.1


with open('left', 'r') as f:
    x = []
    y = []
    z = []
    z_ave = []
    for line in f:
       # print(len(line))
        if len(line) > 4:

            x1,y1,z1 = line.strip().split(',')
            x.append(x1)
            y.append(y1)
            z.append(z1)
            if len(z_ave) < 1:
                z_ave.append(int(y1))
            else:
                z_ave.append(tiny*int(y1) + (1.0 - tiny)*z_ave[-1])


x_arr = np.array(x)
y_arr = np.array(y)
z_arr = np.array(z)
az = [math.acos( int(i) / 2048) for i in z]
az = np.array(z_ave)
u = np.linspace(0, 330, len(x))
print(len(x_arr))
print(len(u))
print(u)

plt.subplot(421)
plt.plot(u,x_arr)
plt.title('x')
plt.subplot(423)
plt.plot(u,y_arr)
plt.title('y')
plt.subplot(425)
plt.plot(u,z_arr)
plt.title('z')
plt.subplot(427)
plt.plot(u,az)
plt.title('acos z')

with open('right', 'r') as f:
    x = []
    y = []
    z = []
    for line in f:
       # print(len(line))
        if len(line) > 4:

            x1,y1,z1 = line.strip().split(',')
            x.append(x1)
            y.append(y1)
            z.append(z1)

x_arr = np.array(x)
y_arr = np.array(y)
z_arr = np.array(z)
az = [math.acos(int(i) / 2048) for i in z]
az = np.array(az)
u = np.linspace(0, 330, len(x))

plt.subplot(422)
plt.plot(u,x_arr)
plt.title('x')
plt.subplot(424)
plt.plot(u,y_arr)
plt.title('y')
plt.subplot(426)
plt.plot(u,z_arr)
plt.title('z')
plt.subplot(428)
plt.plot(u,az)
plt.title('acos z')
plt.show()