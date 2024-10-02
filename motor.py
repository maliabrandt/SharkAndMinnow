#motor.py
#Malia Brandt and Roberto Garcia 
#For the Shark and Minnow ME35 Project September 2024
#This file contain the motor class. It takes in a parameter indicating whether it 
#is the left or the right motor. It has functions for going forward, turning left, 
#right, and going backwards. 


from machine import Pin, PWM
import time

class motor:
    #itialize pins and variables 
    def __init__(self, side):
        #know which motor you are
        self.side = side
        #set duty cycle and frequency 
        self.f = 500
        self.d = 60000
        #for motor left
        if self.side == 'left':
            self.pin_one = Pin('GPIO13', Pin.OUT)
            self.pin_two = Pin('GPIO14', Pin.OUT)
            self.pwm = PWM(Pin('GPIO15', Pin.OUT))
            self.pwm.freq(self.f)
            self.pwm.duty_u16(self.d)

        #for motor right
        elif self.side == 'right':
            self.pin_one = Pin('GPIO17', Pin.OUT)
            self.pin_two = Pin('GPIO18', Pin.OUT)
            self.pwm = PWM(Pin('GPIO16', Pin.OUT))
            self.pwm.freq(self.f)
            self.pwm.duty_u16(self.d)


    #spin forward
    def forward(self):
        self.pin_one.high()
        self.pin_two.low()

    #spin backwards
    def back(self):
        self.pin_one.low()
        self.pin_two.high()
    
    #turn both off
    def off(self):
        self.pin_one.low()
        self.pin_two.low()
        
    #turn left
    def left(self):
        print('going left')
        if self.side == 'right':
            self.forward()
        elif self.side == 'left':
            self.off()
    
    def right(self):
        print('going right')
        if self.side == 'right':
            self.off()
        elif self.side == 'left':
            self.forward()
        