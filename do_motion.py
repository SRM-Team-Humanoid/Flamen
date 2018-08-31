from time import sleep
from Read import Read
from Dynamixel import Dynamixel
from Equations import Equations

'''constrints for m3 & m4- (-132.4, 140.91)'''


if __name__=='__main__':
	dxl=Dynamixel()
	'''x1,y1=379,173
	x2,y2=385,447

	x1,y1=Equations.pixel_to_real(x1,y1)
	x2,y2=Equations.pixel_to_real(x2,y2)'''
	x1,y1,x2,y2=28,5,5,5
	try:
		th1,th2,th3=Equations.get_th(x1,y1,x2,y2)
		if th2>130 or th2<-130 or th3<-130 or th3>130:
			raise "Mechanical constraint...exiting"
		print th1,th2,th3
		raw_input()

	except ValueError:
		raise "Out of range...stopping\n"

	#th1,th2,th3=34.32423,43.23423,56.54523
	motion_set=Read.read_from_file("mot.txt",th1,th2,th3)

	for motion in motion_set:
		dxl.set_position(motion[0])
		sleep(motion[1])
		#print motion[0],"\t\t\t",motion[1]
