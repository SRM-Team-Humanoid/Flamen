from math import sqrt,atan,acos,degrees,pi,asin,sin,tan,cos

class Equations:

	@staticmethod
	def pixel_to_real(x,y):
		Y=17*2.54
		X=23*2.54

		x=(x-640/2)
		y=-(y-(480))


		x= (x*(X/640))
		y= (y*(Y/480))

		return x,y

	@staticmethod
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
