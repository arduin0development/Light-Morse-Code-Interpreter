import serial
import os

from Tkinter import * 

dict = {'01'   : 'A', '1000' : 'B', '1010' : 'C',
        '100'  : 'D', '0'    : 'E', '0010' : 'F',
        '110'  : 'G', '0000' : 'H', '00'   : 'I',
        '0111' : 'J', '101'  : 'K', '0100' : 'L',
        '11'   : 'M', '10'   : 'N', '111'  : 'O',
        '0110' : 'P', '1101' : 'Q', '010'  : 'R',
        '000'  : 'S', '1'    : 'T', '001'  : 'U',
        '0001' : 'V', '011'  : 'W', '1001' : 'X',
        '1011' : 'Y', '1100' : 'Z'}
code = ""
message = ""
serialPort = '/dev/ttyACM0'

try:  
    arduino = serial.Serial(serialPort, 9600)  
    print "Connexion arduino OK !"
    
except:  
    print "Failed to connect on "+serialPort 

while(1):
    msg =""
    try :
        msg = arduino.read()
        if(msg=='3'):
            message = message + dict.get(code)
            os.system('clear')
            print message
            code = ""
        elif(msg=='2'):
						message= message.rstrip(message[-1:])
						os.system('clear')
						print message
						code = ""
        else:
        		code = code + msg
    except :
				os.system('clear')
				print message
				print"code incorrect"
				code = ""
