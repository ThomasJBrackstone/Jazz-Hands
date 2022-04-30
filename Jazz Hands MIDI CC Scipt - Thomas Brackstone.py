from microbit import *
import math

def midiControlChange(chan, n, value):
    MIDI_CC = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_CC | chan, n, value])
    uart.write(msg)

def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

Start()
last_tilt = 0
while True:

    current_tilt = accelerometer.get_y()
    if current_tilt != last_tilt:
        mod_y = math.floor(math.fabs((((current_tilt + 1024) / 2048) * 127)))
        midiControlChange(1, 22, mod_y)
        last_tilt = current_tilt

    current_tilt = accelerometer.get_x()
    if current_tilt != last_tilt:
        mod_x = math.floor(math.fabs((((current_tilt + 1024) / 2048) * 127)))
        midiControlChange(1, 21, mod_x)
        last_tilt = current_tilt

    sleep(10)

