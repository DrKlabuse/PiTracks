
import RPi.GPIO as GPIO
from CTrack import CTrack
from CTrackDrive import CTrackDrive
from ITrackDrive import EDriveCmd
from ITrackDrive import EDriveSpeed
import time
import sys
import os
#import wiringpi
from evdev import InputDevice, categorize, ecodes

# GPIO IDs verwenden
GPIO.setmode(GPIO.BCM)

track_left = CTrack(23, 24, 12)
print("Track left created")
track_right = CTrack(14, 15, 13)
print("Track right created")

trackDrive = CTrackDrive(track_left, track_right)
print("TrackDrive created")
trackDrive.start()

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
up = 292
down = 294
left = 295
right = 293
startBtn = 291
selectBtn = 288

# loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == up: # Vor
                trackDrive.cmd(EDriveCmd.EDCMD_MOVEFORWARD)
                trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
                print("Vor")
                time.sleep(0.01)

            elif event.code == right:  # Rechts
                trackDrive.cmd(EDriveCmd.EDCMD_TURNRIGHT)
                trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
                print("Rechts")
                time.sleep(0.01)

            elif event.code == left:  # Links
                trackDrive.cmd(EDriveCmd.EDCMD_TURNLEFT)
                trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
                print("Links")
                time.sleep(0.01)

            elif event.code == down:  # Links
                trackDrive.cmd(EDriveCmd.EDCMD_MOVEBACKWARD)
                trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
                print("Zurueck")
                time.sleep(0.01)

            elif event.code == startBtn:  # pause
                print("Ende")
                break

trackDrive.cmd(EDriveCmd.EDCMD_STOP)
trackDrive.cleanup()
GPIO.cleanup()
