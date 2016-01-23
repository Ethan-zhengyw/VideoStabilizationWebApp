import cv2
import numpy as np


def add_kps(iimg):
    oimg = np.ndarray(iimg.shape)

    surf = cv2.xfeatures2d.SURF_create()

    (kps, descs) = surf.detectAndCompute(iimg, None)

    oimg = cv2.drawKeypoints(iimg, kps[:200], np.ndarray(iimg.shape))

    return oimg


def draw(input, output):
    iimg = cv2.imread(input)
    oimg = np.ndarray(iimg.shape)

    surf = cv2.xfeatures2d.SURF_create()

    (kps, descs) = surf.detectAndCompute(iimg, None)

    oimg = cv2.drawKeypoints(iimg, kps, np.ndarray(iimg.shape))

    cv2.imwrite(output, oimg)


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

draw('../images/window/window.jpg', '../images/window/window_kps.png')