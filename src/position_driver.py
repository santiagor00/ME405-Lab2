"""!
@package docstring
Lab 2 - Out of Control

@file position_driver.py
"""

class PositionDriver:
    
    def __init__(self):
        self.kp = 1
        self.setpoint = 256

    def run(self,posnow, setpoint = 8675309, kp = 8675309):
        if kp != 8675309: self.kp = kp/1000
        if setpoint != 8675309: self.end = setpoint

        self.now = posnow
        self.error = self.end - self.now
        #print(self.error)
        level = self.error * self.kp

        if level > 100:
            level = 100
        elif level < -100:
            level = -100

        return level

    def set_setpoint(self,setpoint):
        self.end = setpoint

    def set_kp(self,kp):
        self.kp = kp