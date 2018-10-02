# yeah, its the same as rMinus but I couldn't
# find the code so i wrote this again
# it would have taken me more time to find it


# positive angle - anticlockwise rotation
import pypot.dynamixel
from time import sleep
class Dynamixel:
	def __init__(self):
		ports=pypot.dynamixel.get_available_ports()
		if not ports :
			raise IOError("No ports found")

		print "Connecting to ",ports[0]
		self.dxl=pypot.dynamixel.DxlIO(ports[0])
		self.ids=self.dxl.scan(range(25))
		print self.ids

		self.set_speed(75)
		self.initial_position()

	def initial_position(self):
		#self.set_speed(20)

		#self.set_position( [0,80,-90,-90,-90,0,0] )
		#sleep(5)
		#self.set_position( [0,80,-90,-90,90,0,0] )
		#sleep(5)
		self.set_position( [0,0,-90,-80,90,0,0] )

		raw_input(__name__ + " press enter to continue ")
		self.set_speed(70)

	def set_speed(self,speed):
		speeds=[speed]
		speeds=speeds*len(self.ids)
		speed_dict=dict(zip(self.ids,speeds))
		self.dxl.set_moving_speed(speed_dict)

	def set_position(self,positions):
		position_dict=dict(zip(self.ids,positions))
		self.set_speed(70)
		self.dxl.set_goal_position(position_dict)
