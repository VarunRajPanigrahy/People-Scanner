import os
import video_maker
import frame_maker
import face_crop
import predictor

video_maker.make_video()
frame_maker.make_frame()
face_crop.crop_face()
predictor.predict_faces()
