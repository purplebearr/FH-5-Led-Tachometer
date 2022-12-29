from gpiozero import LED
from time import sleep
import socket
import struct

print('Make sure your Raspberry Pi is connected to the internet.')

#getting info from user
local_ip = str(input("Input Ip Adress of Raspberry Pi: "))
port_no = int(input("Input a free port number here: "))

print("Make sure to input the Ip", local_ip, "and port number", port_no, "into Forza.")

#Setting up the Raspberry Pi to recieve information from Forza as the info broadcasted is a UDP packet
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((local_ip, port_no))


#Binding leds to GPIO pins
led10 = LED(26)
led9 = LED(3)
led8 = LED(4)
led7 = LED(5)
led6 = LED(6)
led5 = LED(7)
led4 = LED(8)
led3 = LED(9)
led2 = LED(10)
led1 = LED(11)

def main():
    message, address = server.recvfrom(1024)
    data = struct.unpack('<iI27f4i20f6i19fH6B4b', message) #unpacking data from Forza
    maxRPM = (data[2])
    currentRPM = (data[4])

    #checking if the player is in game first
    if maxRPM > 0:
        percentage_tach = currentRPM / maxRPM *100
            
        if percentage_tach >=10:
            led1.on()
        else:
            led1.off()
        if percentage_tach >=20:
            led2.on()
        else:
            led2.off()
        if percentage_tach >=30:
            led3.on()
        else:
            led3.off()
        if percentage_tach >=40:
            led4.on()
        else:
            led4.off()
        if percentage_tach >=50:
            led5.on()
        else:
            led5.off()
        if percentage_tach >=60:
            led6.on()
        else:
            led6.off()
        if percentage_tach >=69:
            led7.on()
        else:
            led7.off()
        if percentage_tach >=79:
            led8.on()
        else:
            led8.off()
        if percentage_tach >=88:
            led9.on()
        else:
            led9.off()
        if percentage_tach >=93:
            led10.on()
        else:
            led10.off()
    elif maxRPM == 0:
        pass
    else:
        pass


if __name__ == '__main__':
    try:
        while True:
            main()

    except Exception as e:
        print("Sorry, an error occurred. Did you inputing information again.")
        print(e)
    finally:
        pass
