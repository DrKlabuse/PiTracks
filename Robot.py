
import RPi.GPIO as GPIO
from CTrack import CTrack
from CTrackDrive import CTrackDrive
from ITrackDrive import EDriveCmd
from ITrackDrive import EDriveSpeed
import time
import pygame
import sys
import os
#import wiringpi

# GPIO IDs verwenden
GPIO.setmode(GPIO.BCM)

track_left = CTrack(23, 24, 12)
print("Track left created")
track_right = CTrack(14, 15, 13)
print("Track right created")

trackDrive = CTrackDrive(track_left, track_right)
print("TrackDrive created")
trackDrive.start()

os.environ["SDL_VIDEODRIVER"]="dummy"
pygame.init()
pygame.display.init()
pygame.display.set_mode((1,1))

j = pygame.joystick.Joystick(0)
j.init()

try:
    while j.get_button(3) == 0:
        # pygame.event.pump()
        pygame.event.get()

        if j.get_button(4) != 0: # Vor
            trackDrive.cmd(EDriveCmd.EDCMD_MOVEFORWARD)
            trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
            print("Vor")
            time.sleep(0.01)

        elif j.get_button(5) != 0: # Rechts
            trackDrive.cmd(EDriveCmd.EDCMD_TURNRIGHT)
            trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
            print("Rechts")
            time.sleep(0.01)

        elif j.get_button(7) != 0: # Links
            trackDrive.cmd(EDriveCmd.EDCMD_TURNLEFT)
            trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
            print("Links")
            time.sleep(0.01)

        elif j.get_button(6) != 0: # Zurueck
            trackDrive.cmd(EDriveCmd.EDCMD_MOVEBACKWARD)
            trackDrive.setSpeed(EDriveSpeed.EDSPD_FAST)
            print("Zurueck")
            time.sleep(0.01)

        elif j.get_button(4) == 0 or j.get_button(5) == 0 or j.get_button(6) == 0 or j.get_button(7) == 0:
            trackDrive.cmd(EDriveCmd.EDCMD_STOP)
            print("Stillstand")

    trackDrive.cmd(EDriveCmd.EDCMD_STOP)
    trackDrive.cleanup()
    GPIO.cleanup()

except KeyboardInterrupt:
    trackDrive.cmd(EDriveCmd.EDCMD_STOP)
    trackDrive.cleanup()
    GPIO.cleanup()

