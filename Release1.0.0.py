from gpiozero import LED
from time import sleep
import socket
import struct
from tkinter import *
import tkinter as tk
import sys

local_ip = 0
port_no = 0

#Binding leds to GPIO pins
led10 = LED(12)
led9 = LED(3)
led8 = LED(4)
led7 = LED(5)
led6 = LED(6)
led5 = LED(7)
led4 = LED(8)
led3 = LED(9)
led2 = LED(10)
led1 = LED(11)

#Gui for getting information from the user
def getInfo():
    def button_command():
        global local_ip
        local_ip = str(entry1.get())
        global port_no
        port_no = int(entry2.get())
        root.destroy()

    root = tk.Tk()
    root.geometry("500x250")
    root.title("Setup")

    label1 = tk.Label(root, text="Enter IP Address of Raspberry Pi: ", font=('Arial', 14))
    label1.pack(padx=20, pady=20)

    entry1 = Entry(root, width=20)
    entry1.pack()

    label2 = tk.Label(root, text="Enter a free port number: ", font=('Arial', 14))
    label2.pack(padx=20, pady=20)

    entry2 = Entry(root, width=20)
    entry2.pack()

    Button(root, text="Submit", command=button_command).pack()

    root.mainloop()

def reminder():
    def button_command1():
        root.destroy()

    root = tk.Tk()
    root.geometry("500x250")
    root.title("Setup")
    text1 = "Make sure to input the Ip " + local_ip + " and port number " + str(port_no) + " into Forza."

    label1 = tk.Label(root, text=text1, font=('Arial', 10))
    label1.pack(padx=20, pady=20)

    Button(root, text="Confirm", command=button_command1).pack()

    root.mainloop()

def errorMessage(errorcode):
    def button_command2():
        root.destroy()

    root = tk.Tk()
    root.geometry("600x250")
    root.title("Error")
    text1 = "An error occurred. Try making sure all modules are downloaded, or inputing information again."
    text2 = str(errorcode)

    label1 = tk.Label(root, text=text1, font=('Arial', 10))
    label1.pack(padx=20, pady=20)

    label2 = tk.Label(root, text=text2, font=('Arial', 10))
    label2.pack(padx=20, pady=20)

    Button(root, text="Close", command=button_command2).pack()

    root.mainloop()

def main():
    getInfo()
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #setting up Raspberry Pi to recieve UDP packet from Forza
    server.bind((local_ip, port_no))
    reminder()

    while True:
        message, address = server.recvfrom(1024)
        data = struct.unpack('<iI27f4i20f6i19fH6B4b', message)  # unpacking data from Forza
        maxRPM = (data[2])
        currentRPM = (data[4])

        #Checking if the player is in game first, if player is in menu maxRPM will be equal to zero and cause an error
        if maxRPM > 0:
            percentage_tach = currentRPM / maxRPM * 100 #calculations

            if percentage_tach >= 10:
                led1.on()
            else:
                led1.off()
            if percentage_tach >= 20:
                led2.on()
            else:
                led2.off()
            if percentage_tach >= 30:
                led3.on()
            else:
                led3.off()
            if percentage_tach >= 40:
                led4.on()
            else:
                led4.off()
            if percentage_tach >= 50:
                led5.on()
            else:
                led5.off()
            if percentage_tach >= 60:
                led6.on()
            else:
                led6.off()
            if percentage_tach >= 69:
                led7.on()
            else:
                led7.off()
            if percentage_tach >= 79:
                led8.on()
            else:
                led8.off()
            if percentage_tach >= 88:
                led9.on()
            else:
                led9.off()
            if percentage_tach >= 93:
                led10.on()
            else:
                led10.off()
        elif maxRPM == 0:
            pass
        else:
            pass

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        errorMessage(e)
    finally:
        sys.exit()
