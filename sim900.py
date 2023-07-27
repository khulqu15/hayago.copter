import time
import serial

class SIM900:
    def __init__(self, port, baudrate,timeout):
        self.mPort = port
        self.mPBaudrate=baudrate
        self.mTimeout=timeout
        
    def connect(self):
        try:
            self.mConn = serial.Serial(port=self.mPort,baudrate=self.mPBaudrate,timeout=self.mTimeout)
            return True
        except Exception as e:
            print(str(e))
            return False


    def call(self,phoneNumber):
        try:
            #print ("Set call mode")
            #port.write("AT+CMGF=0\r".encode())
            time.sleep(1)
            print ("Start call")

            cmd = "ATD{};\r".format(phoneNumber)
            self.mConn.write(cmd.encode())
            time.sleep(30)
            print ("End call")
        except Exception as e:
            print(str(e))
            return False


    def sendMessage(self,phoneNumber,msg):
        try:
            self.mConn.write('AT+CMGF=1\r'.encode())
            time.sleep(0.5)

            cmd = 'AT + CMGS = \"{}\"\r'.format(phoneNumber)
            self.mConn.write(cmd.encode()); 
            time.sleep(0.5);

            cmd = '{}\r'.format(msg)
            self.mConn.write(cmd.encode()); 
            time.sleep(0.5);

            self.mConn.write(bytes([26]))

            time.sleep(0.5);

            return True
        except Exception as e:
            print(str(e))
            return False

    def disconnect(self):
        try:
            self.mConn.close()
            return False
        except Exception as e:
            print(str(e))
            return False

if __name__=="__main__":
    sim = SIM900("/dev/ttyAMA0",19200,1.0)
    sim.connect()
    #sim.call()
    sim.sendMessage("+62895396004952","ConnectDisconnect")
    sim.disconnect()