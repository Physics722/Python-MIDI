import rtmidi
import serial

ser = serial.Serial('COMPORT', baudrate=31250)  # Adjust the baudrate as needed (MIDI standard is 31250).

midi_out = rtmidi.MidiOut()
midi_out.open_virtual_port("Virtual MIDI Port")
