import serial, time  
import matplotlib.pyplot as plt
import numpy as np
import sys
port = "/dev/ttyACM0"  
baud = 115200  
s = serial.Serial(port)  
s.baudrate = baud

left_values = []
right_values = []

def collect_values(seconds):
    left_values = []
    right_values = []
    start = time.time()

    while (time.time() - start < seconds):  
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
    
    return left_values, right_values

def get_moving_average(values, tiny=0.2):
    x = []
    y = []
    z = []
    x_ave = []
    y_ave = []
    z_ave = []
    for item in values:
            x1,y1,z1 = item.strip().split(',')
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
        

print('Please sit with good posture for several seconds.')
input('Press enter to start')
left, right = collect_values(4)
print('Calibration complete')
print(left)
left_ave = get_moving_average(left)
right_ave = get_moving_average(right)

for item in left_ave:
    #print(min(item), max(item))
    diff = max(item) - min(item)
    if diff > 50:
        print('Error, too much movement in calibration. Please try again. (Restart)')
        sys.exit()

for item in right_ave:
    #print(min(item), max(item))
    diff = max(item) - min(item)
    if diff > 50:
        print('Error, too much movement in calibration. Please try again. (Restart)')
        sys.exit()
        
left = []
right = []
left_track = []
right_track = []
for i in range(3):
    left.append(np.mean(left_ave[i]))
    right.append(np.mean(right_ave[i]))
    left_track.append(np.mean(left_ave[i]))
    right_track.append(np.mean(right_ave[i]))

#print(left, right)

# start measurement

left_values = []
right_values = []

tiny = 0.1
threshold = 100
time_threshold = 4
start = time.time()
timer_left = [None, None, None]
timer_right = [None, None, None]
posture_flag = 0
bad_posture_start = 0
total_bad_posture_time = 0
time_written = 0

with open('log', 'w') as f:

    while True:
        
        data = s.readline()
        current_time = time.time()
        #print(data)
        tokens = data.decode('utf-8').split(", ")
        f.write(','.join(tokens))
        if int(current_time) % 10 == 0:
            if time_written == 0:
                f.write('ctime,%f' % (current_time - start))
                time_written = 1
        else:
            time_written = 0
            
        if (len(tokens) == 4):
           # print(tokens)
            (name,x,y,z) = tokens
            if (name == 'Left'):
                left_values.append(','.join([x,y,z]))
                for i in range(3):
                    left_track[i] = tiny*float(tokens[i+1]) + (1-tiny)*left_track[i]
                    if abs(left_track[i] - left[i]) > 100:
                        if timer_left[i] is None:
                            timer_left[i] = current_time
                            print('danger zone')
                        if current_time - timer_left[i] > time_threshold:
                            if posture_flag == 0:
                                posture_flag = 1
                                bad_posture_start = timer_left[i]
                                print('bad posture start!')
                    else:
                        timer_left[i] = None
                        if posture_flag == 1:
                            # check if any other timers are active
                            timer_flag = 0
                            for timer in timer_left:
                                if timer is not None:
                                    timer_flag = 1
                                    break
                            
                            if timer_flag == 0:
                                for timer in timer_right:
                                    if timer is not None:
                                        timer_flag = 1
                                        break
                            
                            if timer_flag == 0:
                                posture_flag = 0
                                total_bad_posture_time += current_time - bad_posture_start
                                f.write('badp,%f' % total_bad_posture_time)
                                print('good posture :)')
                            
                        
                        
            elif (name == 'Right'):
                right_values.append(','.join([x,y,z]))
                for i in range(3):
                    right_track[i] = tiny*float(tokens[i+1]) + (1-tiny)*right_track[i]
                    if abs(right_track[i] - right[i]) > 100:
                        if timer_right[i] is None:
                            timer_right[i] = current_time
                            print('danger zone')
                        if current_time - timer_right[i] > time_threshold:
                            if posture_flag == 0:
                                posture_flag = 1
                                bad_posture_start = timer_right[i]
                                print('bad posture start!')
                    else:
                        timer_right[i] = None
                        if posture_flag == 1:
                            # check if any other timers are active
                            timer_flag = 0
                            for timer in timer_left:
                                if timer is not None:
                                    timer_flag = 1
                                    break
                            
                            if timer_flag == 0:
                                for timer in timer_right:
                                    if timer is not None:
                                        timer_flag = 1
                                        break
                            
                            if timer_flag == 0:
                                posture_flag = 0
                                total_bad_posture_time += current_time - bad_posture_start
                                f.write('badp,%f' % total_bad_posture_time)
                                print('good posture :)')