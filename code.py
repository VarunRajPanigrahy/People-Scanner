# import the necessary packages
#from skimage.measure import structural_similarity as ssim
from skimage import measure
#import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err
def compare_images(imageA, imageB):
	m = mse(imageA, imageB)
	s = measure.compare_ssim(imageA, imageB)
	return s

def similarity(img1,img2):
	original = cv2.imread(img1)
	contrast = cv2.imread(img2)
	original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
	contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
	return(compare_images(original, contrast))


while(True):
	folder="CTD"
	test_imgs_list=os.listdir(folder)

	img_path="CTD/"+test_imgs_list[0]
	max_sim=0.25
	name="None"
	students=os.listdir("Training Data")
	for s in students:
		imgs=os.listdir("Training Data/%s"%(s))
		for i in imgs:
			img="Training Data/%s/%s"%(s,i)
			sim_now=similarity(img_path,img)
			if(sim_now>max_sim):
				max_sim=sim_now
				name=s

	os.remove(img_path)
	if(name==None):continue
	file=open('Attendance.txt','r')
	present=dict()
	for line in file:
		if(line):
			stu=line.split(" ")[0]
			sta=line.split(" ")[1]
			present[stu]=sta

	file.close()
	file=open('Attendance.txt','w')
	for s in present:
		w=""
		if(s==name):
			w="%s P\n"%(s)
		else:
			w="%s %s"%(s,present[s])
		file.write(w)





