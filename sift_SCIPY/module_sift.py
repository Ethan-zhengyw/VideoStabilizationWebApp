# -*- coding: utf-8 -*-

import cv2
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

    # count, n = 0, 100
    xs, ys = [], []
    for m in matches:

        if m.distance > 5.0:
            continue

        kp1 = kps1[m.queryIdx]
        kp2 = kps2[m.trainIdx]

        bias_x = kp2.pt[0] - kp1.pt[0]
        bias_y = kp2.pt[1] - kp1.pt[1]

        if not (-100 < bias_x < 100 and -100 < bias_y < 100):
            continue

        # print('bias x: %f, bias y: %f' % (bias_x, bias_y))

        xs.append(bias_x)
        ys.append(bias_y)

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
        # count += 1
        # if count == n:
        #     break


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
            else:
                next_frame_copy[i, j] = (0, 0, 0)

    return next_frame_copy


def add_kps_to_img(in_img, n=-1):

    surf = cv2.xfeatures2d.SURF_create()
    (kps, desc) = surf.detectAndCompute(in_img, None)

    if n == -1 or n > len(kps):
        n = len(kps)

    out_img = cv2.drawKeypoints(in_img, kps[:n], np.ndarray(in_img.shape))

    return out_img


def draw_kps_match(img1, img2):

    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SURF_create()

    # find the key points and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    matches = bf.match(des1, des2)
    matches_sorted = sorted(matches, key=lambda x: x.distance)

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches1to2=matches_sorted[:200], outImg=np.ndarray(img1.shape))

    return img3


def my_draw_kps(iimg, kps):

    for kp in kps:
        x, y = int(kp.pt[0]), int(kp.pt[1])
        for xx in range(x - 10, x + 10):
            for yy in range(y - 10, y + 10):
                if 0 < xx < iimg.shape[1] and 0 < yy < iimg.shape[0]:
                    iimg[yy, xx] = (255, 0, 0)

    return iimg


def my_draw_kps_2(iimg, kps):

    for kp in kps:
        x, y = int(kp.pt[0]), int(kp.pt[1])
        for xx in range(x - 10, x + 10):
            for yy in range(y - 10, y + 10):
                if 0 < xx < iimg.shape[1] and 0 < yy < iimg.shape[0]:
                    iimg[yy, xx] = (0, 255, 0)

    return iimg


def connect_two_img(left, right):

    h, w = left.shape[0], left.shape[1]

    con = np.ndarray((h, w * 2, 3))

    con[:h, :w] = left.copy()
    con[:h, w:w * 2] = right.copy()

    return con
