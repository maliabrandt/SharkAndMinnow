This GitHub page contain the code for the shark and minnow car game. 
It has:
- a file to run on the ME35 website for TM, where thumbs up turns the car on and thumbs down turns the car off. 
- a file to run in OpenMV (for the camer) that processes April Tags and sends MQTT messages for the car the receive. 
- two files to run on the Pico, one containing a motor class, and one containing a receive_motor_info class

The motor class takes left or right motor input, and has left, right, forward, and backward commands.
The receive_motor_info class receives mqtt commands and calls motor functions based on the commands. 
