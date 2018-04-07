from microbit import *
import radio

class Measurement(object):

    def __init__(self, name, acc_x, acc_y, acc_z):
        self.name = name
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z
    
    def __str__
        print(name + str(acc_x) + ", " + str(acc_y) + ", " + str(acc_z) + "\n")
        
        

radio.on()
radio.config(channel = 41)
radio.config(power=7) 

display.show("Hi")

while True:
    
    acc_string = radio.receive()
    #if (tokens[0] == "LS"):
        
    if acc_string is not None:
        tokens = acc_string.split(", ") 
        print(acc_string)
        Test = Measurement(tokens[0],tokens[1],tokens[2],tokens[3])
        print("All is going well!")
        print(Test)