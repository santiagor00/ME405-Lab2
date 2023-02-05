This directory contains code to perform step response tests on electric motors. 
The main PC program will ask the user to input Kp values, which represent the proportional gain 
on the feedback loop for encoder position. After receiving a Kp value from the user, the main PC 
program will send the Kp value to the MCU. 

Then, the main MCU program will run a step response on the electric motor. 
The main MCU program sends position data to the PC program, which will create a
plot of position vs. time.

![Everything graph](https://user-images.githubusercontent.com/122561488/216850585-818e5f8e-ea35-4ff9-aa0a-b4d629850ad4.png)

Figure 1: For a Kp value of 5, the system exhibited underdamped behavior as seen in the plot. There was almost no 
oscillation. For a Kp value of 15, the system underwent a "perfectly damped" response, which can be seen in the single 
overshoot that precedes the steady state behavior. A Kp value of 50 led to the excesive oscillations seen in an overdamped 
system.
