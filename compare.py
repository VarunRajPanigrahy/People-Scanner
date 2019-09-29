import numpy as np
import cv2
from PIL import Image
import os

def detect_face(img):
    #convert the test image to gray image as opencv face detector expects gray images
    image=cv2.imread(img)
    gray = cv2.cvtColor((image), cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return gray[y:y+w, x:x+h],faces[0]
'''
img="1.1.jpg"
x=detect_face(img)
img1 = Image.fromarray(x[0], 'L')
#print(type(img1[0]))
cv2.imwrite("newfile.jpg",x[0])

'''
def prepare():
	train=os.listdir("Training Data")
	faces=[]
	labels=[]
	for img in train:
		face=detect_face("Training Data/"+img)
		if face is not None:
			faces.append(face)
			l=img.split(".")[0]
			labels.append(int(l))

	return faces,labels

faces,labels=prepare()
print(type(faces[0]))
faces=tuple(faces)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

