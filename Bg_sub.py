import numpy as np
import cv2
import math
from skimage.measure import compare_ssim

class Bg_sub:
	@staticmethod
	def bg_sub():
		cap=cv2.VideoCapture(3)
		ret=True
		while ret:
			ret,cam=cap.read()
			#yuv=cv2.cvtColor(cam,cv2.COLOR_BGR2YUV)
			cv2.imshow("yuv",cam)
			#mask = cv2.inRange(cam, (np.array([97,46,17])), (np.array([117,46,17])))
			if cv2.waitKey(5)==ord("c"):
				cv2.imwrite("img/without_fan.jpg",cam)
				print 'without fan'
			if cv2.waitKey(5)==ord("d"):
				cv2.imwrite("img/with_fan.jpg",cam)
				print 'with fan'
			if cv2.waitKey(5)==27:
				break
		cap.release()
		cv2.destroyAllWindows()

		image1 = cv2.imread("img/without_fan.jpg")
		image2 = cv2.imread("img/with_fan.jpg")
		grayA = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
		grayB = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
		#cv2.imwrite("grayA.jpg",grayA)
		#cv2.imwrite("grayB.jpg",grayB)
		(score, diff) = compare_ssim(grayB, grayA, full=True)
		diff = (diff * 255).astype("uint8")
		thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		blur = cv2.GaussianBlur(thresh,(5,5),1)
		kernel = np.ones((5,5),np.uint8)
		erode = cv2.erode(blur,kernel,iterations = 1)
		dilate = cv2.dilate(erode,kernel,iterations = 1)
		#cv2.imwrite("diff.jpg",diff)
		#cv2.imwrite("dilate.jpg",dilate)n
		img1,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
		for c in contours:
			if cv2.contourArea(c)>1000:
				x,y,w,h=cv2.boundingRect(c)
				print "width", w, "height", h
				cv2.rectangle(image2,(x,y),(x+w,y+h),[255,0,0],1)
				cv2.drawContours(image2, c, -1, (0,255,0), 2)
				if max(w,h)==w:
					roi1 = dilate[y:(y+h), x:(x+(w/2))]
					roi2 = dilate[y:(y+h),(x+(w/2)):(x+w)]
					#cv2.imwrite("ROI1.jpg",roi1)
					#cv2.imwrite("ROI2.jpg",roi2)
					im1 = np.asarray(roi1, dtype=np.float)
					im2 = np.asarray(roi2, dtype=np.float)
					sum1= im1.sum()
					sum2=im2.sum()
					if sum1>sum2:
						top1=tuple(c[c[:, :, 1].argmin()][0])
						bottom1=tuple(c[c[:, :, 0].argmin()][0])
						if top1[0]<320:
							top1=tuple(c[c[:, :, 0].argmin()][0])
							bottom1=tuple(c[c[:, :, 1].argmax()][0])
						cv2.circle(image2, top1, 3, (255, 0, 0), -1)
						cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
						print "Top: ",top1
						print "Bottom: ",bottom1
					else:
						top1=tuple(c[c[:, :, 0].argmin()][0])
						bottom1=tuple(c[c[:, :, 1].argmax()][0])
						if top1[0]>320:
							 top1=tuple(c[c[:, :, 1].argmin()][0])
							 bottom1=tuple(c[c[:, :, 0].argmin()][0])
						print "been there"
						cv2.circle(image2, top1, 3, (255, 0, 0), -1)
						cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
						print "Top: ",top1,"else_part"
						print "Bottom: ",bottom1

					print "hori"
				else:
					roi1=dilate[y:(y+(h/2)),x:x+w]
					roi2=dilate[(y+(h/2)):y+h,x:x+w]
					#cv2.imwrite("ROI1.jpg",roi1)
					#cv2.imwrite("ROI2.jpg",roi2)
					im1 = np.asarray(roi1, dtype=np.float)
					im2 = np.asarray(roi2, dtype=np.float)
					sum1= im1.sum()
					sum2=im2.sum()
					if sum1>sum2:
						top1=tuple(c[c[:, :, 1].argmin()][0])
						bottom1=tuple(c[c[:, :, 0].argmin()][0])
						if top1[0]<320:
							 top1=tuple(c[c[:, :, 0].argmin()][0])
							 bottom1=tuple(c[c[:, :, 1].argmax()][0])
						print "been here"
						cv2.circle(image2, top1, 3, (255, 0, 0), -1)
						cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
						print "Top: ",top1
						print "Bottom: ",bottom1
					else:
						top1=tuple(c[c[:, :, 1].argmin()][0])
						bottom1=tuple(c[c[:, :, 0].argmin()][0])
						if top1[0]< 320:
							top1=tuple(c[c[:, :, 0].argmin()][0])
							bottom1=tuple(c[c[:, :, 1].argmax()][0])
						cv2.circle(image2, top1, 3, (255, 0, 0), -1)
						cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
						print "Top: ",top1
						print "Bottom: ",bottom1
					print "vert"

				if w>65:
					output=(top1,bottom1,"Tedha")
				else:
					output=(top1,bottom1,"Seedha")
				
		cv2.imwrite("img/final.jpg",image2)

		cv2.waitKey(0)

		return output
