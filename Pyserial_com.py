import serial

ser = serial.Serial('COM3', 9600)  # open the serial port
while True:
    input_value = input("Enter A or B: ")  # get input from the user
    if input_value == 'A':
        ser.write(b'A')  # send the character 'A'
    elif input_value == 'B':
        ser.write(b'B')  # send the character 'B'
    else:
        print("Invalid input.")
ser.close()
