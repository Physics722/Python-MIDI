import machine
import serial

ser = serial.Serial('COMPORT', baudrate=31250)  # Adjust the baudrate as needed (MIDI standard is 31250).

def send_midi_message(status, data1, data2):
    midi_message = bytes([status, data1, data2])
    ser.write(midi_message)
