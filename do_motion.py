from math import sqrt,atan,acos,degrees,pi,asin,sin,tan,cos
import pypot.dynamixel
from time import sleep


'''constrints for m3 & m4- (-132.4, 140.91)'''

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
	x1,y1=28,5
	x2,y2=5,5
	
	try:
		th1,th2,th3=get_th(x1,y1,x2,y2)
		print th1,th2,th3
		raw_input()
		file=open("mot.txt",'r')
		angles=file.read()

		print angles
		angles=angles.replace('m1',str(th1))
		angles=angles.replace('m2',str(th2))
		angles=angles.replace('m3',str(th3))
		print angles
		ang_list=angles.split('\n')

		for li in ang_list:
			anglesl=li.split()
			try:
				ang_dict={1:float(anglesl[0]),2:float(anglesl[1]),3:float(anglesl[2]),4:float(anglesl[3]),5:float(anglesl[4]),6:float(anglesl[5]),7:float(anglesl[6])}
				dxl.set_goal_position(ang_dict)
			except Exception as e:
				print e
			sleep(2)
	except ValueError:
		print "out of range"
