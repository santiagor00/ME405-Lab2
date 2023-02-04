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
import serial





    
def main():

    """!
    @brief Prepare the pins, timers, and everything necessary, then run the motor while reading the encoder.
    """
    
#     pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.OUT_PP) 
#     tim4 = pyb.Timer (4, freq=30)
#     ch1 = tim4.channel (1, pyb.Timer.ENC_AB, pin=pinB6)

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

    pdriver.run(encreader.read(),100000,50)

    time = array.array("i",300*[0])
    pos = array.array("i",300*[0])

    n = 0

    with serial.serial("COM3",115200) as ser:
        while not(ser.any()):
            pass
        ser.readline()
        ser.readline()
        ser.readline()

        timestart = utime.ticks_ms()

        try:
            while True:
                #print("COUNTER", tim8.counter())
                #print(encreader.read())
                utime.sleep_ms(10)
                posnow = encreader.read()
                level = pdriver.run(posnow)
                mdriver.set_duty_cycle(level)
                timenow = utime.ticks_ms()
                if n != 300:
                    time[n] = utime.ticks_diff(timenow,timestart)
                    pos[n] = posnow
                    n += 1
                #print(f"position = {posnow}")

        except KeyboardInterrupt:
            mdriver.set_duty_cycle(0)
            for i in range(n):
                print(time[i],",",pos[i])


if __name__ == '__main__':
    main()

