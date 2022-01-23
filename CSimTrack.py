
import ITrack

class CSimTrack( ITrack.ITrack ):
	
	Dir = ITrack.ETrackDir.ETDIR_FORWARD

	def __init__(self):
		self.stop()

	def printTrack(self):
		pass

	def start(self):
		pass

	def stop(self):
		pass

	def setDirection(self, dir, blub):
		pass

	def setSpeed(self, speed):
		pass

	def cleanup(self):
		pass
 
