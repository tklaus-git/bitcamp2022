import numpy as np
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import mediapipe

video = cv2.VideoCapture(1)
if (video.isOpened() == False):
  print("Error opening video stream or file")

detector = FaceMeshDetector(maxFaces=1)

plotY= LivePlot(640, 360, [20, 50])


idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]

while True:

    success, img = video.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 5, (255, 0, 255), cv2.FILLED)
        leftUp = face[159]
        leftDown = face[23]

        leftLeft = face[130]
        leftRight = face[243]

        distanceVert, _ = detector.findDistance(leftUp, leftDown)
        distanceHor, _ = detector.findDistance(leftLeft, leftRight)

        distanceVert = (distanceVert/distanceHor)*100

        print(int(distanceVert))
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)

        if distanceHor<12:
            print('\nBLINK\n')

    cv2.imshow('Image', img)
    cv2.waitKey(1)




#           1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27
letters = ['','E','T','I','A','N','M','S','U','R','W','D','K','G','O','H','V','F','','L','','P','J','B','X','C','Y','Z','Q','','']
dots = [0,0,1,1]

# dots is a list of 0's and 1's; 0: short blink, 1: long blink
def letter(dots):
    trace = 1
    for dot in dots:
        if dot == 0:
            trace = 2*trace
        else:
            trace = (2*trace)+1
            
    if letters[trace-1] == '' and trace%2 == 1:
        trace = (trace-1)/2
    elif letters[trace-1] == '' and trace%2 == 0:
        trace = trace/2
        
    return letters[int(trace-1)]

print(letter(dots))