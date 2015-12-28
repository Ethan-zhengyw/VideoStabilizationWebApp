import cv2
import numpy as np
#import pdb
#pdb.set_trace()#turn on the pdb prompt

#read image
img = cv2.imread('Helene.png',cv2.IMREAD_COLOR)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('origin',img);

#SIFT
detector = cv2.SIFT()
keypoints = detector.detect(img,None)
img = cv2.drawKeypoints(img,keypoints)
#img = cv2.drawKeypoints(gray,keypoints,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('test',img);
cv2.waitKey(0)
cv2.destroyAllWindows()
