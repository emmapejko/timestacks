import cv2 as cv
import numpy as np
import sys
# import matplotlib.pyplot as plt
# import time

#video reader
video_name = sys.argv[1]
cap = cv.VideoCapture(video_name)

#initialize image for timestack
fps = int(cap.get(cv.CAP_PROP_FPS))
length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
height = int(cap.get(4)) #height is same as height of input video
width = length
timestack_img = np.zeros((height, width, 3), dtype="uint8")

print(timestack_img.shape)

#choose a column to look at
k = 500
#counter for timestack x-axis
x_axis = 0
#take each frame and select one column of pixels and write to timestack image
while(1):
	#take each frame
	ret,frame = cap.read()

	#print(frame.shape)

	if ret == True:
		if x_axis < width:
			#select kth column
			#add to timestack image
			timestack_img[:,x_axis] = frame[:,k]

			#increment counter
			x_axis += 1

	else:
		break


	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break

#write image to png file
output_file = video_name + '_timestack.png'
cv.imwrite(output_file, timestack_img)

cap.release()
cv.destroyAllWindows()