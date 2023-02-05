## Program Description
This directory contains code to perform step response tests on electric motors. The main PC program will ask the user to 
input Kp values, which represent the proportional gain on the feedback loop for encoder position. After receiving a Kp 
value from the user, the main PC program will send the Kp value to the MCU. This directory contains code to perform step 
response tests on electric motors. Data transmission from the PC to the MCU is done through the VCP (Virtual Com 
Port), which allows data to be transmitted in the form of bytes.

Then, the main MCU program will run a step response on the electric motor. 
The main MCU program sends position data to the PC program, which will create a
plot of position vs. time. Data from the MCU is sent through UART2. UART stands for universal 
asynchronous receiver-transmitter, and UART2 allows serial transmission of data from the MCU
to the PC while the VCP is simultaneously free to send data from the PC to the MCU.

![Everything graph](https://user-images.githubusercontent.com/122561488/216850585-818e5f8e-ea35-4ff9-aa0a-b4d629850ad4.png)

## Figure 1: Time Vs. Position
For a Kp value of 5, the system exhibited underdamped behavior as seen in the plot. There was almost no 
oscillation. For a Kp value of 15, the system underwent a "perfectly damped" response, which can be seen in the single 
overshoot that precedes the steady state behavior. A Kp value of 50 led to the excesive oscillations seen in an overdamped 
system.
