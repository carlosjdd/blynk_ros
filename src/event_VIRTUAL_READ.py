#!/usr/bin/python

import BlynkLib
import time

BLYNK_AUTH = 'gASisGlaGebx-uTQn6zKU0H1Fw45v4aj'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register virtual pin handler
@blynk.on("readV2")
def v2_read_handler():
    # This widget will show some time in seconds..
    blynk.virtual_write(2, time.ticks_ms() // 1000)

while True:
    blynk.run()
