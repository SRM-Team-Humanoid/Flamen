#########################################################################################################
# Copyright 2018 SRM Team Humaniod
# All Rights Reserved
#
# Licensed under the ApashyamKiriKiri License, Version 1.13.[insertRandomNumberHere]
# you may not use this file except in compliance with the License.
# 
# This is a proprietry code. No one except the Team Leads, Domain Heads
# or Coding Domain Senior Balak or Balikas of SRMTH are supposed to read this.
#
# If you are not a Team Lead, Domain Head or Coding Domain Senior Balak or Balika
# your eyes will pop out in the next 5 seconds.
#
# No one except the Owners have the right to access or modify the code.
#
#########################################################################################################

# Owner     : SRM Team Humaniod, Kattankulathur
# Author    : Akarsh Shrivastava
# Maintainer: No one tries to maintain this.
#
# Yes I was so jobless that I did all this

from time import sleep,time
from Read import Read
from Dynamixel import Dynamixel
from Equations import Equations
from Bg_sub import Bg_sub

'''constrints for m3 & m4- (-132.4, 140.91)'''


if __name__=='__main__':
	dxl=Dynamixel()
	
	detection=Bg_sub.bg_sub()
	x1,y1,x2,y2=detection[0][0],detection[0][1],detection[1][0],detection[1][1]

	x1,y1=Equations.pixel_to_real(x1,y1)
	x2,y2=Equations.pixel_to_real(x2,y2)
	th1,th2,th3=Equations.get_th(x1,y1,x2,y2)
	print "coordinates - ", x1,y1,x2,y2
	print "angles - ", th1,th2,th3
	
	raw_input("press Enter to continue ")
	
	if th2>130 or th2<-130 or th3<-130 or th3>130:
		th11,th22,th33=Equations.get_th(x1,y1,x2,y2, point_of_grasp=11)
		motion_set=Read.read_from_file("close.mot",th11-2,th22,th33)

		for motion in motion_set:
			dxl.set_position(motion[0])
			sleep(motion[1])

	else:
		motion_set=Read.read_from_file("normal.mot",th1,th2,th3)

		for motion in motion_set:
			dxl.set_position(motion[0])
			sleep(motion[1])




	motion_set=Read.read_from_file("flap.mot",th1,th2,th3)
	
	for motion in motion_set:
		dxl.set_position(motion[0])
		sleep(motion[1])









	'''signs=[
				[1,1,1],
				[1,1,-1],
				[1,-1,1],
				[1,-1,-1],
				[-1,1,1],
				[-1,1,-1],
				[-1,-1,1],
				[-1,-1,-1]
	]
	
	dxl.set_position([0,85,0,0,-90,-90,0])
	
	for sign in signs:
		th11,th22,th33=sign[0]*th1,sign[1]*th2,sign[2]*th3
		dxl.set_position([th11,85,th22,th33,-90,-90,0])
		print sign
		raw_input("press enter to for next ")
	
	'''
