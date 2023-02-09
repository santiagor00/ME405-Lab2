"""!@package docstring
@file main.py
@brief This code runs a motor and reads from the encoder
@details This code uses timers 3,5,and 8, and pins PC6,PC7,PA10,PB4, and PB5 to controll a motor and an encoder

@author Team01
@date 1-18-22
"""

import pyb
import utime
import motor_driver
import encoder_reader
import position_driver
import array
from pyb import repl_uart
from pyb import UART




    
def main():

    """!
    @brief Prepare the pins, timers, and everything necessary, then waits for serial input to run the motor while reading the encoder. Sends data from encoder over serial once complete.
    @details prepares timers and pins to read encoder and send PWM to motor. Waits for serial input of kp and end position from computer main on UART2, runs the motor with these values, then sends encoder data back over UART2.
    """
    


    tim8 = pyb.Timer (8, prescaler=0, period=0xFFFF)
    tim3 = pyb.Timer (3, freq=20000)
    tim5 = pyb.Timer (5, freq=20000)

    pinC6 = pyb.Pin (pyb.Pin.board.PC6, pyb.Pin.OUT_PP) 
  
    pinC7 = pyb.Pin (pyb.Pin.board.PC7, pyb.Pin.OUT_PP)
      
      
    encreader = encoder_reader.EncoderReader(pinC6, pinC7, tim8)
      
    ENA = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
    IN1A = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    IN2A = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
      
    ENA.high()
      
    mdriver = motor_driver.MotorDriver(ENA, IN1A, IN2A, tim3)
    pdriver = position_driver.PositionDriver()
      
    p = True

    

    time = array.array("i",300*[0])
    pos = array.array("i",300*[0])

    n = 0
    start = "a"
    waiter = 0

    repl_uart(None)


    ser = UART(2,115200)
    while start != "start":
        while waiter == 0:
            waiter = ser.any()
        startbyte = ser.read(5)
        
        start = startbyte.decode()

        utime.sleep_ms(5)
    
    kp = ser.readline()
    endpos = ser.readline()


    kp = kp.decode()
    endpos = endpos.decode()

    kp = kp.strip()
    endpos = endpos.strip()

    kp = int(kp)
    endpos = int(endpos)

    pdriver.run(encreader.read(),endpos,kp)

    timestart = utime.ticks_ms()

    try:
        while n <= 299:

            utime.sleep_ms(15)
            posnow = encreader.read()
            level = pdriver.run(posnow)
            mdriver.set_duty_cycle(level)
            timenow = utime.ticks_ms()
            if n != 300:
                time[n] = utime.ticks_diff(timenow,timestart)
                pos[n] = posnow
                n += 1


    except KeyboardInterrupt:
        mdriver.set_duty_cycle(0)
        for i in range(n):
            print(time[i],",",pos[i])
    
    mdriver.set_duty_cycle(0)
    for i in range(n):
        ser.write(f"{time[i]},{pos[i]}\r \n")


if __name__ == '__main__':
    while True:
        main()


