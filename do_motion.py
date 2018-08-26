import pypot.dynamixel
from math import sqrt,atan,acos,degrees,pi,asin,sin,tan,cos
from time import sleep
from read import read_from_file

'''constrints for m3 & m4- (-132.4, 140.91)'''

Y=17*2.54
X=23*2.54

def init():
	ports=pypot.dynamixel.get_available_ports()
	if not ports :
		raise IOError("No ports found")

	print "Connecting to ",ports[0]

	global dxl
	dxl=pypot.dynamixel.DxlIO(ports[0])
	ids=dxl.scan(range(25))
	dxl.set_moving_speed({1:70,2:70,3:70,4:70,5:70,6:70,7:70})
	print ids

	dxl.set_goal_position({1:0, 2:0, 3:-90, 4:-90, 5:90, 6:0, 7:0})

	raw_input()

def pixel_to_real(x,y):
	x=(x-640/2)
	y=-(y-(480))
	
	
	x= (x*(X/640))
	y= (y*(Y/480))
	
	return x,y


def get_th(x1,y1,x2,y2):
	l1=9.3
	l2=7


	tha=float(atan((y1-y2)/(x1-x2)))
	x=(x2+2*cos(tha))
	y=(y2+2*sin(tha))
	dist=float(sqrt((x*x)+(y*y)))
	th2=float(acos(((dist*dist) - (l1*l1) - (l2*l2))/(2*l1*l2)))
	d1=float(acos(y/dist))
	d2=float(acos((dist**2 + l1**2 - l2**2)/(2*l1*dist)))
	th1=(d1-d2)
	th3=pi/2-tha-th1-th2
	return (degrees(th1),-degrees(th2),-degrees(th3))
	#return (0,-45,-45)




if __name__=='__main__':
	init()
	x1,y1=379,173
	x2,y2=385,447
	
	x1,y1=pixel_to_real(x1,y1)
	x2,y2=pixel_to_real(x2,y2)
	
	try:
		th1,th2,th3=get_th(x1,y1,x2,y2)
		print th1,th2,th3
		raw_input()		

	except ValueError:
		raise "Out of range...stopping\n"

	#th1,th2,th3=34.32423,43.23423,56.54523
	motion_set=read_from_file("mot.txt",th1,th2,th3)
	
	for motion in motion_set:
		dxl.set_goal_position(motion[0])
		sleep(motion[1])
		#print motion[0],"\t\t\t",motion[1]
