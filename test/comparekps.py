# -*- coding: utf-8 -*-

import cv2
import kps
import numpy as np


def adjust_frame(cur_frame, next_frame):

    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SURF_create()

    # find the key points and descriptors with SIFT
    kps1, des1 = sift.detectAndCompute(cur_frame, None)
    kps2, des2 = sift.detectAndCompute(next_frame, None)

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    matches = bf.match(des1, des2)

    # matches_sorted = sorted(matches, key=lambda x: x.distance)
    # print(len(matches_sorted))

    n = 0
    xs, ys = [], []
    for m in matches:

        if m.distance > 1.0:
            continue

        kp1 = kps1[m.queryIdx]
        kp2 = kps2[m.trainIdx]

        bias_x = kp2.pt[0] - kp1.pt[0]
        bias_y = kp2.pt[1] - kp1.pt[1]

        if not (-10 < bias_x < 10 and -10 < bias_y < 10):
            continue

        # print('bias x: %f, bias y: %f' % (bias_x, bias_y))

        xs.append(bias_x)
        ys.append(bias_y)

        n += 1
        if n == 10:
            break
        # cv2.imshow('sss', cur_frame)
        # cv2.waitKey()
        # cv2.imshow('sss', next_frame)
        # cv2.waitKey()
        #
        # next_frame = my_draw_kps(next_frame, [kp1])
        # cv2.imshow('sss', next_frame)
        # cv2.waitKey()
        #
        # next_frame = my_draw_kps_2(next_frame, [kp2])
        # cv2.imshow('sss', next_frame)
        # cv2.waitKey()



        # print(kp2.pt[0] - kp1.pt[0], kp2.pt[1] - kp1.pt[1])
    # print()
    # xs.sort()
    # ys.sort()
    # x, y = np.mean(xs[24:75]), np.mean(ys[24:75])
    x, y = int(round(np.mean(xs))), int(round(np.mean(ys)))
    print(x, y)

    next_frame_copy = next_frame.copy()
    h, w = next_frame.shape[0], next_frame.shape[1]
    for i in range(h):
        for j in range(w):
            if 0 < i + y < h and 0 < j + x < w:
                next_frame_copy[i, j] = next_frame[i + y, j + x]

    return next_frame_copy


in_video = cv2.VideoCapture('C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/mingde/input2.avi')


frames = []
for i in range(10):
    frames.append(in_video.read()[1])

frame_ = adjust_frame(frames[1], frames[2])

sift = cv2.xfeatures2d.SURF_create()

kps1, des1 = sift.detectAndCompute(frames[1], None)
kps2, des2 = sift.detectAndCompute(frame_, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(des1, des2)
# matches_sorted = sorted(matches, key=lambda x: x.distance)

kps1_, kps2_ = [], []

oimg = frames[1]
for m in matches:

    if m.distance > 0.3:
        continue

    kp1 = kps1[m.queryIdx]
    kp2 = kps2[m.trainIdx]

    print(m.distance)
    oimg = kps.my_draw_kps(oimg, [kp1])
    cv2.imshow('out', oimg)
    cv2.waitKey()

    oimg = kps.my_draw_kps_2(oimg, [kp2])

    cv2.imshow('out', oimg)
    cv2.waitKey()

cv2.imwrite('img.png', oimg)
cv2.waitKey()