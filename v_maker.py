import numpy as np
import cv2
import time

# The duration in seconds of the video captured
x=0
while(True):
	capture_duration = 5

	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FPS, 1)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('Video/output_%d.avi'%(x),fourcc,10.0, (640,480))
	x+=1
	start_time = time.time()
	while( int(time.time() - start_time) < capture_duration ):
	    ret, frame = cap.read()
	    if ret==True:
	        out.write(frame)
	        
	        #cv2.imshow('frame',frame)
	    
	    else:
	        break

	cap.release()
	out.release()
	cv2.destroyAllWindows()