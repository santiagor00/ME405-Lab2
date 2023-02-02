class PositionDriver:
    
    def __init__(self):
        self.kp = 1
        self.setpoint = 256

    def run(self,posnow, setpoint = "N", kp = "N"):
        if kp != "N": self.kp = kp
        if setpoint != "N": self.end = setpoint

        self.now = posnow
        self.error = self.end - self.end
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