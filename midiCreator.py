import mido
from mido import Message

msg = Message('note_on', note=60)
outport = mido.open_output("New Port", virtual="True")
inport = mido.open_input()
outport.send(msg)