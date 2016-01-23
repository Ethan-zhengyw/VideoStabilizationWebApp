import cv2
import numpy as np

img1 = cv2.imread('../images/draw/draw.jpg')          # queryImage
img2 = cv2.imread('../images/draw2/draw2.jpg')   # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SURF_create()

# find the key points and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(des1, des2)
matches_sorted = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches1to2=matches_sorted[:200], outImg=np.ndarray(img1.shape))
cv2.imwrite('match.png', img3)
cv2.waitKey()