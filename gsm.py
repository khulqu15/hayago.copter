import serial   
import os, time
 
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

port.write('AT\r\n'.encode())
rcv = port.read(10)
print(rcv)