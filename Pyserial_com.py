import serial

ser = serial.Serial('COM3', 9600)  # porta
while True:
    input_value = input("Insira A ou B,ENTER para finalizar. ")
    if input_value == 'A':
        ser.write(b'A')  # Envia A/como byte
    elif input_value == 'B':
        ser.write(b'B')  # Envia B/como byte
    elif input_value == ''
         break
    else:
        print("Inválido.")
ser.close()# fecha porta serial
