#!/usr/bin/env python3

import time, random
import math
from collections import deque

import matplotlib.pyplot as plt
import numpy as np

import serial

start = time.time()

class RealtimePlot:
    def __init__(self, axes, max_entries = 100):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.axes = axes
        self.max_entries = max_entries
        
        self.lineplot, = axes.plot([], [], "ro-")
        self.axes.set_autoscaley_on(True)
    
    def add(self, x, y):
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.lineplot.set_data(self.axis_x, self.axis_y)
        self.axes.set_xlim(self.axis_x[0], self.axis_x[-1] + 1e-15)
        self.axes.relim(); self.axes.autoscale_view() # rescale the y-axis
    
    def animate(self, figure, callback, interval = 50):
        import matplotlib.animation as animation
        def wrapper(frame_index):
            self.add(*callback(frame_index))
            self.axes.relim(); self.axes.autoscale_view() # rescale the y-axis
            return self.lineplot
        animation.FuncAnimation(figure, wrapper, interval=interval)
        

def measure(s):
    data = s.readline()
    print(data)
    tokens = data.decode('utf-8').split(", ")
    if (len(tokens) == 4):
        print(tokens)
        (name,x,y,z) = tokens
        if (name == 'Left'):
            return float(y)

def main():

    port = "/dev/ttyACM1"  
    baud = 115200  
    s = serial.Serial(port)  
    s.baudrate = baud

    x_left_values = []
    x_right_values = []
    '''while True:  
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
                
            elif (nam    fig = plt.figure()e == 'Right'):
                x_right_values.append(x)
                x_r = np.array(x_right_values)
                plt.plot(x_r)
                plt.title('right')
                plt.show()'''
    
    fig, axes = plt.subplots()
    display = RealtimePlot(axes)
    display.animate(fig, lambda frame_index: (time.time() - start, measure(s)))
    plt.show()
    
    fig, axes = plt.subplots()
    display = RealtimePlot(axes)
    while True:
        display.add(time.time() - start, measure(s))
        plt.pause(0.001)

if __name__ == "__main__": main()
