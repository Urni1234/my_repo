import serial

ser = serial.Serial(port = 'COM3',baudrate = 9600)

while True:
    val = ser.readline()
    valueInString = str(val , 'UTF-8')
    print(valueInString)