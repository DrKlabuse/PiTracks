
import abc

from enum import Enum

class ETrackDir(Enum):
    ETDIR_FORWARD = 1
    ETDIR_BACKWARD = 2

class ITrack( abc.ABC ):

	@abc.abstractclassmethod
	def start(self):
		pass

	@abc.abstractclassmethod
	def stop(self):
		pass

	@abc.abstractclassmethod
	def setDirection(self, dir):
		pass

	@abc.abstractclassmethod
	def setSpeed(self, speed):
		pass

	@abc.abstractclassmethod
	def cleanup(self):
		pass
 
