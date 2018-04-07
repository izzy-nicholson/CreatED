import serial

with serial.Serial('/dev/cu.usbmodem1422', 115200) as ser:
    while True:
        s = ser.readline()        # read up to ten bytes (timeout)
        print(s)
