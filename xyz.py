import os
import cv2
from PIL import Image

def detect_face(img):
    
    image=cv2.imread(img)
    gray = cv2.cvtColor((image), cv2.COLOR_BGR2GRAY)
    
    
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3);
    
    
    if (len(faces) == 0):
        return None, None
    ret=[]
    
    for i in range(len(faces)):
        (x, y, w, h) = faces[i]
        
        
        ret.append(gray[y:y+w, x:x+h])
    return ret

imgs=os.listdir("Frames")
for i in imgs:
    

    img="Frames/%s"%(i)
    print(img)
    try:
        z=detect_face(img)
        for x in z:
            if x is not None:
               
                
                y=cv2.resize(x,(128,128))

                cv2.imwrite("CTD/%s"%(i),y)
    except:
        pass
    try:
        os.remove(img)
    except FileNotFoundError:
        pass
imgs=os.listdir("Frames")
for i in imgs:
    img="Frames/%s"%(i)
    os.remove(img)
