import face_recognition
import cv2
import numpy as np

video = cv2.VideoCapture(0)
if (video.isOpened() == False):
  print("Error opening video stream or file")

while True:
    ret, frame = video.read()
    cv2.imshow('frame', frame)
    cv2.waitKey(1)