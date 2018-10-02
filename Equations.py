from math import sqrt,atan,acos,degrees,pi,asin,sin,tan,cos

class Equations:

	@staticmethod
	def pixel_to_real(x,y):
		REAL_Y=17*2.54			# height of working area
		REAL_X=23*2.54			# width  of working area

		PXL_Y=480				# height of camera frame
		PXL_X=640				# width  of camera frame

		PXL_CEN_X=335
		PXL_CEN_Y=480

		x=  (x - PXL_CEN_X)			# shifting
		y= -(y - PXL_CEN_Y)			# the origin


		x= (x * (REAL_X/PXL_X))
		y= (y * (REAL_Y/PXL_Y))

		return x,y

	@staticmethod
	def get_th(x1,y1,x2,y2, poi=-1):
		l1=9.3
		l2=7
		print "x1,y1 = ",x1, y1
		print "x2,y2 = ",x2, y2
		print "point",poi

		tha=float(atan((y1-y2)/(x1-x2)))
		if	tha<0:
			tha+=pi
		xj=(x2+(poi*cos(tha)))
		#print "xj",xj,x2,cos(tha)
		yj=(y2+(poi*sin(tha)))

		print "xj,yj = ",xj,yj
		dist=float(sqrt((xj*xj)+(yj*yj)))
		print "dist = ",dist
		print -((dist*dist) - (l1*l1) - (l2*l2))/(2*l1*l2)
		th2= pi - float(acos(-((dist*dist) - (l1*l1) - (l2*l2))/(2*l1*l2)))
		print "th2 = ",th2
		d1=float(acos(xj/dist))
		print "d1 = ",degrees(d1)
		d2=float(acos((dist**2 + l1**2 - l2**2)/(2*l1*dist)))
		print "d2 = ",degrees(d2)
		th1= pi/2-(d1+d2)
		print "th1 = ",degrees(th1)
		#if tha<0:
		#	tha+=pi
		print "tha = ",degrees(tha)
		th3=pi/2-tha-th1-th2

		return (-degrees(th1),-degrees(th2),-degrees(th3))
		#return (0,-45,-45)
