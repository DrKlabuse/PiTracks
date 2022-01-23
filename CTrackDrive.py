
import ITrackDrive
from ITrackDrive import EDriveCmd
from ITrackDrive import EDriveSpeed

import ITrack
from ITrack import ETrackDir

class CTrackDrive(ITrackDrive.ITrackDrive):
	
	TrackLeft = None
	TrackRight = None
	Speed = ITrackDrive.EDriveSpeed.EDSPD_SLOW
	SpeedInt = 30;
	LastCmd = ITrackDrive.EDriveCmd.EDCMD_STOP

	def __init__(self, track_left, track_right):
		self.TrackLeft = track_left
		print("TrackObject assigned for left")
		self.TrackRight = track_right
		print("TrackObject assigned for right")

	def start(self):
		self.TrackLeft.start()
		self.TrackRight.start()

	def cleanup(self):
		self.TrackLeft.cleanup()
		self.TrackRight.cleanup()

	def cmd(self, cmd):
		if (cmd == EDriveCmd.EDCMD_TURNLEFT):
			self.turnLeft()
		elif (cmd == EDriveCmd.EDCMD_TURNRIGHT):
			self.turnRight()
		elif (cmd == EDriveCmd.EDCMD_MOVEFORWARD):
			self.moveForward()
		elif (cmd == EDriveCmd.EDCMD_MOVEBACKWARD):
			self.moveBackward()
		elif (cmd == EDriveCmd.EDCMD_STOP):
			self.stop()
		else:
			return
		self.LastCmd = cmd

	def setSpeed(self, speed):
		self.Speed = speed
		self.SpeedInt = 0
		if(speed == EDriveSpeed.EDSPD_FASTEST):
			self.SpeedInt = 100
		elif(speed == EDriveSpeed.EDSPD_FAST):
			self.SpeedInt = 95
		elif(speed == EDriveSpeed.EDSPD_MEDIUM):
			self.SpeedInt = 90
		elif(speed == EDriveSpeed.EDSPD_SLOW):
			self.SpeedInt = 85
		elif(speed == EDriveSpeed.EDSPD_SLOWEST):
			self.SpeedInt = 80
		self.TrackLeft.setSpeed(self.SpeedInt)
		self.TrackRight.setSpeed(self.SpeedInt)

	def turnLeft(self):
		self.TrackLeft.setDirection(ETrackDir.ETDIR_BACKWARD)
		self.TrackRight.setDirection(ETrackDir.ETDIR_FORWARD)

	def turnRight(self):
		self.TrackLeft.setDirection(ETrackDir.ETDIR_FORWARD)
		self.TrackRight.setDirection(ETrackDir.ETDIR_BACKWARD)

	def	moveForward(self):
		self.TrackLeft.setDirection(ETrackDir.ETDIR_FORWARD)
		self.TrackRight.setDirection(ETrackDir.ETDIR_FORWARD)

	def	moveBackward(self):
		self.TrackLeft.setDirection(ETrackDir.ETDIR_BACKWARD)
		self.TrackRight.setDirection(ETrackDir.ETDIR_BACKWARD)

	def stop(self):
		self.TrackLeft.stop()
		self.TrackRight.stop()
