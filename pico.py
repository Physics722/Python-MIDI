import machine
import serial

ser = serial.Serial('COMPORT', baudrate=31250)  # Adjust the baudrate as needed (MIDI standard is 31250).
