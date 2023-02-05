This directory contains code to perform step response tests on electric motors. 
The main PC program will ask the user to input Kp values, which represent the proportional gain 
on the feedback loop for encoder position. After receiving a Kp value from the user, the main PC 
program will send the Kp value to the MCU. 

Then, the main MCU program will run a step response on the electric motor. 
The main MCU program sends position data to the PC program, which will create a
plot of position vs. time.

![Everything graph](https://user-images.githubusercontent.com/122561488/216850585-818e5f8e-ea35-4ff9-aa0a-b4d629850ad4.png)

kp too low was 5, kp too high was 50, and perfect kp was 15
