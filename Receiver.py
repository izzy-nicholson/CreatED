from microbit import *
import radio

class Measurement(object):

    def __init__(self, name, acc_x, acc_y, acc_z):
        self.name = name
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z
    
    def __str__(self):
        print(str(self.name) +": "+ str(self.acc_x) + ", " + str(self.acc_y) + ", " + str(self.acc_z))
        
radio.on()
radio.config(channel = 41)
radio.config(power=7) 

display.show("C")

time_list=[]
left_list=[]
right_list =[]
centre_list =[]

for t in range(500):
        
    acc_string = radio.receive()
       
    if acc_string is not None:

        tokens = acc_string.split(", ") 
        Test = Measurement(tokens[0],tokens[1],tokens[2],tokens[3])
        print(Test)
        if(tokens[0]=="Left"):
            if(len(left_list) - len(right_list) <1):
                left_list.append(Test)
                t += 1
        elif (tokens[0] == "Right"):
            if(len(right_list) - len(left_list) <1):
                right_list.append(Test)

while True:
               
    acc_string = radio.receive()
           
    if acc_string is not None:

        tokens = acc_string.split(", ") 
        Test = Measurement(tokens[0],tokens[1],tokens[2],tokens[3])
        print(Test)
        if(tokens[0]=="Left"):
            if(len(left_list) - len(right_list) <1):
                del(left_list[0])
                left_list.append(Test)
                t += 1
                centre_list.append(Measurement(Centre, accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z())
        elif (tokens[0] == "Right"):
            if(len(right_list) - len(left_list) <1):
                del(right_list[0])
                right_list.append(Test)
                
    if(t%500==0):
        print("The length of the left list is: " + str(len(left_list)))        
        print("The length of the right list is: " + str(len(right_list)))


                
            
        