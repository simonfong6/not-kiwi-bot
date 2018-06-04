"""
ultrasonic.py

Ultrasonic (HCSR04) part for Donkeycar framework.

@author: Saurabh Kulkarni
"""

import serial

#send a stop signal when something is less than 50cm away
THRESHOLD = 50

class HCSR04:
    '''
    Ultrasonic sensor
    '''
    def __init__(self,port='/dev/ttyACM0'):

        #do some inits here I guess???
        self.ser = serial.Serial(port, 9600)
        self.d1 = 500
        self.d2 = 500
        self.on = True

    #blocking single-run version
    def run(self):
        #get the two distances from the arduino via serial
        #distances are in centimeters
        self.ser.reset_input_buffer()
        self.d1, self.d2 = self.ser.readline().strip().split()
        #returns output stop_cmd
        return min(self.d1, self.d2) > THRESHOLD

    #this gets called after an update
    #blindly return the values
    def run_threaded():
        #returns stop_cmd
        return min(self.d1, self.d2) > THRESHOLD
    #independent thread version
    def update(self):
        while self.on:
            #get the two distances from the arduino via serial
            #distances are in centimeters
            self.ser.reset_input_buffer()
            self.d1, self.d2 = self.ser.readline().strip().split()

    def shutdown(self):
        #nothing to do here really
        self.on = False
        return
        
def _main():
    """
    Run with or without a port specified.
    
    python ultrasonics.py
    
    OR
    
    python ultrasonics.py /dev/tty.usbmodem14531
    
    """
    ultrasonics = None
    
    from sys import argv
    
    if(len(argv) > 1):
        port = argv[1]
        ultrasonics = HCSR04(port)
    else:
        ultrasonics = HCSR04()
    
    try:
        print("Reading ultrasonics from arduino:")
        while(True):
            d1,d2 = ultrasonics.run()
            
            print("Distance 1: {} cm \nDistance 2: {} cm".format(d1,d2))
    except(KeyboardInterrupt):
        print("Exiting...")

if(__name__ == '__main__'):
    _main()
