import matplotlib.pyplot as plt
import numpy as np
import math

tiny = 0.1

def get_moving_average(values, tiny=0.2):
    x = []
    y = []
    z = []
    x_ave = []
    y_ave = []
    z_ave = []
    for item in values:
            name,x1,y1,z1 = item.strip().split(',')
            x.append(x1)
            y.append(y1)
            z.append(z1)
            if len(z_ave) < 1:
                x_ave.append(int(x1))
                y_ave.append(int(y1))
                z_ave.append(int(z1))
            else:
                x_ave.append(tiny*int(x1) + (1.0 - tiny)*x_ave[-1])
                y_ave.append(tiny*int(y1) + (1.0 - tiny)*y_ave[-1])
                z_ave.append(tiny*int(z1) + (1.0 - tiny)*z_ave[-1])
    
    return x_ave, y_ave, z_ave

with open('log', 'r') as f:
    left = []
    right = []
    badp = 0
    ctime = 0
    for line in f:
        if len(line) > 4:
            if line[0] == 'L':
                left.append(line.strip())
            elif line[0] == 'R':
                right.append(line.strip())
            elif line[0] == 'b':
                badp = line.split(',')[1]
            elif line[0] == 'c':
                ctime = line.split(',')[1]
                

x, y, z = get_moving_average(left)
x_arr = np.array(x)
y_arr = np.array(y)
z_arr = np.array(z)
u = np.linspace(0, 330, len(x))
#print(len(x_arr))
#print(len(u))
#print(u)

print('Total sitting time:,', ctime)
print('Total bad posture time:', badp)
badp = float(badp) / float(ctime)
print('Percent bad posture: %f' % badp)

plt.subplot(421)
plt.plot(u,x_arr)
plt.title('x')
plt.subplot(423)
plt.plot(u,y_arr)
plt.title('y')
plt.subplot(425)
plt.plot(u,z_arr)
plt.title('z')

x,y,z = get_moving_average(right)

x_arr = np.array(x)
y_arr = np.array(y)
z_arr = np.array(z)
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
plt.show()