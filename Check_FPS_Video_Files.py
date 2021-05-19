#This code will help to find FPS of the vidoes
import cv2
import os

#Change the path where video is stored
folder_path = "D:\\Videos"

arr = os.listdir(folder_path)

for video_file in arr:
    cap=cv2.VideoCapture(folder_path+"\\"+video_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("{} => {}".format(video_file,fps))