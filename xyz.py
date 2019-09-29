import os
import cv2
from PIL import Image

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
    ret=[]
    #under the assumption that there will be only one face,
    #extract the face area
    for i in range(len(faces)):
        (x, y, w, h) = faces[i]
        
        #return only the face part of the image
        ret.append(gray[y:y+w, x:x+h])
    return ret


imgs=os.listdir("Frames")
for i in imgs:
    

    img="Frames/%s"%(i)
    print(img)

    z=detect_face(img)
    for x in z:
        if x is not None:
           
            
            y=cv2.resize(x,(128,128))

            cv2.imwrite("CTD/%s"%(i),y)
        #os.remove(img)
