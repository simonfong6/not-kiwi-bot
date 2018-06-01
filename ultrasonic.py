import donkeycar as dk
import serial


class HCSR04:
    '''
    Ultrasonic sensor
    '''
    def __init__(self):

        #do some inits here I guess???
        this.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.d1 = 500
        self.d2 = 500

    #blocking single-run version
    def run(self):
        #get the two distances from the arduino via serial
        #distances are in centimeters
        this.ser.reset_input_buffer()
        self.d1, self.d2 = this.ser.readline().strip().split()
        return (self.d1, self.d2)

    #this gets called after an update
    #blindly return the values
    def run_threaded:
        return (self.d1, self.d2)
    #independent thread version
    def update(self):
        this.run()

    def shutdown(self):
        #nothing to do here really
        return


