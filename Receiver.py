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

while True:
    
    R = 0    
    L = 0
    time_list=[]
    LS_list=[]
    RS_list =[]
    
    while (R<10):
        
        acc_string = radio.receive()
       
        if acc_string is not None:
            
            print("R = " + str(R))
            print("L = " + str(L))
            
            tokens = acc_string.split(", ") 
            Test = Measurement(tokens[0],tokens[1],tokens[2],tokens[3])
            print(Test)
            if(tokens[0]=="Left"):
                L += 1
            else if (tokens[0] == "Right"):
                R += 1
                 
                
            
        