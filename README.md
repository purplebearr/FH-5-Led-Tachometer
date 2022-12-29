This is a Raspberry Pi powered LED tachometer for Forza Horizon 5 using the "data out" feature. The tachometer is driven by a percentage value of currentRPM/maxRPM which correspond to a light on the tachometer.

To use, enable data out in Forza under "Hud and Gameplay". Make sure wiring is correct, and GPIO pins are wired as they should be. It doesn't really matter which GPIO pins are wired to which number LED, so as long as you remember to change it in the program (LED numbers go from 0-10, with 0 being if the person is in the game menu, 1 being idle, and 10 being at the max engine RPM).

Credit to Michael K. and his blog for information about the data formats. Link -> https://medium.com/@makvoid/building-a-digital-dashboard-for-forza-using-python-62a0358cb43b
