#This class is a simple demo for using a timer task
#A simple LED is turned ON for 3 seconds and then OFF for 2 seconds
import enum
from Utilities.softwaretimer import *

class DFA_Status(enum.Enum):
    INIT = 1
    LED_ON = 2
    LED_OFF = 3

class LedBlinkyTask:

    def __init__(self, _soft_timer):
        self.status = DFA_Status.INIT
        self.soft_timer = _soft_timer
        return

    def LedBlinkyTask_Run(self):
        if self.status == DFA_Status.INIT:
            self.soft_timer.set_timer(0, 3000)
            self.status = DFA_Status.LED_ON
            print("LED is ON")
        elif self.status == DFA_Status.LED_ON:
            if self.soft_timer.is_timer_expired(0) == 1:
                self.status = DFA_Status.LED_OFF
                self.soft_timer.set_timer(0, 2000)
                print("LED is OFF")
        elif self.status == DFA_Status.LED_OFF:
            if self.soft_timer.is_timer_expired(0) == 1:
                self.status = DFA_Status.LED_ON
                self.soft_timer.set_timer(0, 3000)
                print("LED is ON")
        else:
            print("Invalid status!!!")
        return
