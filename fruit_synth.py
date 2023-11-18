# Using the Adafruit's MPR121 capacitive touch board and this guide: https://learn.adafruit.com/adafruit-mpr121-12-key-capacitive-touch-sensor-breakout-tutorial/python-circuitpython
# Install libraries "sudo pip3 install adafruit-circuitpython-mpr121"

# Make sure to replace "sound1.mp3", "sound2.mp3", etc., with the actual paths to your sound files. Also, adjust the pin assignments in the sounds dictionary based on your button configurations.
# This script uses the MPR121 library to detect touch events and Pygame mixer to play the corresponding sound files. The loop continuously checks for touch events and triggers the associated sound when a touch is detected.
# Remember to adapt the script based on your specific needs and hardware setup.

import board
import busio
import adafruit_mpr121
import pygame.mixer
from time import sleep

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize MPR121
mpr121 = adafruit_mpr121.MPR121(i2c)

# Initialize Pygame mixer
pygame.mixer.init()

# Add your sound files and corresponding pins
sounds = {
    0: "sound1.mp3",
    1: "sound2.mp3",
    # Add more as needed
}

def play_sound(pin):
    sound_file = sounds.get(pin)
    if sound_file:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

# Main loop
try:
    while True:
        for i in range(12):
            if mpr121[i].value:
                play_sound(i)
                sleep(0.5)  # Add a delay to avoid repeated triggering
except KeyboardInterrupt:
    pass
finally:
    pygame.mixer.quit()

