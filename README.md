This is a Raspberry Pi powered LED tachometer for Forza Horizon 5 using the "data out" feature. The tachometer is driven by a percentage value of currentRPM/maxRPM which correspond to a LED on the tachometer.

To use, enable data out in Forza under "Hud and Gameplay". Make sure wiring is correct, and GPIO pins and LEDs are wired as they should be. It doesn't really matter which GPIO pins are wired to which number LED, so as long as you remember to change it in the program (LED numbers go from 1-10, 1 being idle, and 10 being at the max engine RPM). If you are in the game menu, all the LED's will turn off untill you return to the game.

Requirements: Raspberry Pi with GPIO pins attached (Raspberry Pi Zero W or better), 10x LEDs, 10x Resistors, wires, and breadboard (optional).

In my build, the following components were used: Raspberry Pi Zero W with GPIO pins attached, 12x wires, 6x green led, 2x yellow led, 2x red led, 10x 1k ohm resistor, and a breadboard. See more details in the wiring diagram.

Video Demonstration: -> https://www.youtube.com/watch?v=xUY6LU_6vyo

Credit to Michael K. and his blog for information about the data formats. Link -> https://medium.com/@makvoid/building-a-digital-dashboard-for-forza-using-python-62a0358cb43b
