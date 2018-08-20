from math import sqrt,atan,acos,degrees,pi,asin,sin,tan,cos
import pypot.dynamixel
from time import sleep




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

	#dxl.set_goal_position({1:0, 2:0, 3:-90, 4:-90, 5:90, 6:0, 7:0})

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
	return (degrees(th1),degrees(th2),-degrees(th3))



if __name__=='__main__':

	init()

	x1=1
	y1=1
	x2=1
	y2=1

	#th1,th2,th3=get_th(x1,y1,x2,y2)


	motion_file=open("motion.txt",'a')

	
	while True:
		try:
			angles=raw_input('Enter angles:')
			anglesl=angles.split()
		except KeyboardInterrupt:
			print 'stopped'
			break

		try:
			ang_dict={1:anglesl[0],2:anglesl[1],3:anglesl[2],4:anglesl[3],5:anglesl[4],6:anglesl[5],7:anglesl[6]}
			dxl.set_goal_position(ang_dict)
		except Exception as e:
			print e
			continue

		dec=raw_input('Enter in file? (y/n) : ')
		if(dec=='y'):
			motion_file.write(angles+'\n')

	
	motion_file.close()
	print "closed"


'''
init pos:
___________________
0 0 -90 -90 90 0 0
'''