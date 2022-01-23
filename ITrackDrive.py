
import abc
from enum import Enum


class EDriveCmd(Enum):
    EDCMD_TURNLEFT = 1
    EDCMD_TURNRIGHT = 2
    EDCMD_MOVEFORWARD = 3
    EDCMD_MOVEBACKWARD = 4
    EDCMD_STOP = 5

class EDriveSpeed(Enum):
    EDSPD_FASTEST = 1
    EDSPD_FAST = 2
    EDSPD_MEDIUM = 3
    EDSPD_SLOW = 4
    EDSPD_SLOWEST = 5


class ITrackDrive( abc.ABC ):

	@abc.abstractclassmethod
	def start(self):
		pass

	@abc.abstractclassmethod
	def cleanup(self):
		pass

	@abc.abstractclassmethod
	def cmd(self, cmd):
		pass

	@abc.abstractclassmethod
	def setSpeed(self, speed):
		pass
