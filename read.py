def read_from_file(filename,th1,th2,th3):
	motion_set=[]
	try:
		file=open(filename,'r')
		angles=file.read()

		angles=angles.replace('m1',str(th1))
		angles=angles.replace('m2',str(th2))
		angles=angles.replace('m3',str(th3))
		motions=angles.split('\n')
		motions=filter(None,motions)
		
		for motion in motions:
			motion_split=motion.split('|')
			r_ang_list,r_wait_time = motion_split[0],motion_split[1]
			ang_list=str(r_ang_list).strip()
			wait_time=str(r_wait_time).strip()

			anglesl=ang_list.split()
			try:
				ang_dict={
							1:float(anglesl[0]),
							2:float(anglesl[1]),
							3:float(anglesl[2]),
							4:float(anglesl[3]),
							5:float(anglesl[4]),
							6:float(anglesl[5]),
							7:float(anglesl[6])
						 }
				motion_set.append([ang_dict,wait_time])
			except Exception as e:
				pass
		
	except IOError:
		raise "File not found\n"

	return filter(None,motion_set)

