import cv2
import os

def FrameCapture(path,saving_path): 
      
     
    vidObj = cv2.VideoCapture(path)

   
    count = 0
  
     
    success = 1

    num=0
  
    while success: 
  
        
        success, image = vidObj.read() 
        tot_img=os.listdir("Frames")
        count=len(tot_img)
        if(num%15==0):
        	cv2.imwrite("%s%d.jpg" % (saving_path, count), image)

        	count += 1
        num+=1
    
def make_frame():
    folder="C:/Users/Varun Raj/Desktop/Syntax Error"
    video_folder="%s/Video"%(folder)
    saving_path="%s/Frames"%(folder)
    print(saving_path)

    f=0
    while(True):
    	videos=os.listdir(video_folder)
    	for v in videos:
    		print(v)
    		video="C:/Users/Varun Raj/Desktop/Syntax Error/Video/"+v
    		s=saving_path+"/frame_%d"%(f)

    		f+=1
    		FrameCapture(video,s)
    		os.remove(video)
    	break




