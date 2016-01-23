# -*- coding: utf-8 -*-
from scipy import misc, ndimage

import test
import numpy as np
import module as md

sss = 'Helene'
typ = 'png'


def detect_local_extrema(pyr_dog):
    """ 检测局部极值

    同一组内，每个像素和它周围的8个像素点以及上下两个不同尺度的周围9+9个像素，
    一共26个像素点进行比较，如果比这26个点的值都大或者都小，
    那么该点就是这幅图像，在横、纵、以及尺度这三个维度空间中的局部极值

    另外根据论文，需要过滤掉特征较弱的点，论文中设置0.03的阈值，
    在这里则需要换算为256*0.03=7.65，所以取8

    """
    threshold = 8

    # img = misc.imread('../images/%s/%s.%s' % (sss, sss, typ)).astype(float)
    # gimg = md.get_gray_2(img)
    pyramid = pyr_dog

    t_pry = test.stub_create_gaussian_pyramid(sss)

    print len(pyramid[0][4]), len(pyramid[0][4][0])
    print len(pyramid[1][4]), len(pyramid[1][4][0])
    print len(pyramid[2][4]), len(pyramid[2][4][0])
    print len(pyramid[3][4]), len(pyramid[3][4][0])

    keypoints = []

    for i in range(4):
        keypoint = [[]] # 差分金字塔第一层无法检测极值
        for j in range(1, 4):

            kps = []

            # cur为目标尺度
            pre, cur, nex = pyramid[i][j - 1], pyramid[i][j], pyramid[i][j + 1]
            h, w = len(cur), len(cur[0])
            print h, w

            for ii in range(1, h - 1):
                for jj in range(1, w - 1):
                    
                    target = cur[ii, jj, 0]
                    if abs(target) > 3:
                        if ((target > cur[ii - 1, jj - 1, 0] and target > cur[ii - 1, jj, 0] and target > cur[ii - 1, jj + 1, 0] and target > cur[ii, jj - 1, 0] and target > cur[ii, jj + 1, 0] and target > cur[ii + 1, jj - 1, 0] and target > cur[ii + 1, jj, 0] and target > cur[ii + 1, jj + 1, 0] and target > pre[ii - 1, jj - 1, 0] and target > pre[ii - 1, jj, 0] and target > pre[ii - 1, jj + 1, 0] and target > pre[ii, jj - 1, 0] and target > pre[ii, jj, 0] and target > pre[ii, jj + 1, 0] and target > pre[ii + 1, jj - 1, 0] and target > pre[ii + 1, jj, 0] and target > pre[ii + 1, jj + 1, 0] and target > nex[ii - 1, jj - 1, 0] and target > nex[ii - 1, jj, 0] and target > nex[ii - 1, jj + 1, 0] and target > nex[ii, jj - 1, 0] and target > nex[ii, jj, 0] and target > nex[ii, jj + 1, 0] and target > nex[ii + 1, jj - 1, 0] and target > nex[ii + 1, jj, 0] and target > nex[ii + 1, jj + 1, 0]) or (target < cur[ii - 1, jj - 1, 0] and target < cur[ii - 1, jj, 0] and target < cur[ii - 1, jj + 1, 0] and target < cur[ii, jj - 1, 0] and target < cur[ii, jj + 1, 0] and target < cur[ii + 1, jj - 1, 0] and target < cur[ii + 1, jj, 0] and target < cur[ii + 1, jj + 1, 0] and target < pre[ii - 1, jj - 1, 0] and target < pre[ii - 1, jj, 0] and target < pre[ii - 1, jj + 1, 0] and target < pre[ii, jj - 1, 0] and target < pre[ii, jj, 0] and target < pre[ii, jj + 1, 0] and target < pre[ii + 1, jj - 1, 0] and target < pre[ii + 1, jj, 0] and target < pre[ii + 1, jj + 1, 0] and target < nex[ii - 1, jj - 1, 0] and target < nex[ii - 1, jj, 0] and target < nex[ii - 1, jj + 1, 0] and target < nex[ii, jj - 1, 0] and target < nex[ii, jj, 0] and target < nex[ii, jj + 1, 0] and target < nex[ii + 1, jj - 1, 0] and target < nex[ii + 1, jj, 0] and target < nex[ii + 1, jj + 1, 0])):
                        # if ((target > 0 and target > cur[ii - 1][jj - 1] and target > cur[ii - 1][jj] and target > cur[ii - 1][jj + 1] and target > cur[ii][jj - 1] and target > cur[ii][jj + 1] and target > cur[ii + 1][jj - 1] and target > cur[ii + 1][jj] and target > cur[ii + 1][jj + 1] and target > pre[ii - 1][jj - 1] and target > pre[ii - 1][jj] and target > pre[ii - 1][jj + 1] and target > pre[ii][jj - 1] and target > pre[ii][jj] and target > pre[ii][jj + 1] and target > pre[ii + 1][jj - 1] and target > pre[ii + 1][jj] and target > pre[ii + 1][jj + 1] and target > nex[ii - 1][jj - 1] and target > nex[ii - 1][jj] and target > nex[ii - 1][jj + 1] and target > nex[ii][jj - 1] and target > nex[ii][jj] and target > nex[ii][jj + 1] and target > nex[ii + 1][jj - 1] and target > nex[ii + 1][jj] and target > nex[ii + 1][jj + 1]) or (target < 0 and target < cur[ii - 1][jj - 1] and target < cur[ii - 1][jj] and target < cur[ii - 1][jj + 1] and target < cur[ii][jj - 1] and target < cur[ii][jj + 1] and target < cur[ii + 1][jj - 1] and target < cur[ii + 1][jj] and target < cur[ii + 1][jj + 1] and target < pre[ii - 1][jj - 1] and target < pre[ii - 1][jj] and target < pre[ii - 1][jj + 1] and target < pre[ii][jj - 1] and target < pre[ii][jj] and target < pre[ii][jj + 1] and target < pre[ii + 1][jj - 1] and target < pre[ii + 1][jj] and target < pre[ii + 1][jj + 1] and target < nex[ii - 1][jj - 1] and target < nex[ii - 1][jj] and target < nex[ii - 1][jj + 1] and target < nex[ii][jj - 1] and target < nex[ii][jj] and target < nex[ii][jj + 1] and target < nex[ii + 1][jj - 1] and target < nex[ii + 1][jj] and target < nex[ii + 1][jj + 1])):
                            kps.append((ii, jj))
                            for iii in range(ii - 2, ii + 3):
                                for jjj in range(jj - 2, jj + 3):
                                    if iii > 0 and jjj > 0 and iii < h and jjj < w:
                                        t_pry[i][j][iii, jjj] = (255, 0, 0)
            misc.imsave('../images/%s/kps_gaussian/' % (sss) + str(i) + '_' + str(j) + '.jpg', t_pry[i][j])
            keypoint.append(kps)
        keypoint.append([])  # 差分金字塔最后一层补上
        keypoints.append(keypoint)
    print keypoints


def create_DOG_pyramid(pyr_gaussian):
    """ 创建高斯差分金字塔
    """
    # octaves = create_gaussian_pyramid(img)
    # octaves = test.stub_create_gaussian_pyramid()
    octaves = pyr_gaussian
    octaves_ = []

    for i in range(4):
        octave = []
        for j in range(5):
            bb = octaves[i][j + 1]
            b = octaves[i][j]
            h, w = b.shape[:2]
            dog = np.ndarray(b.shape)

            img = []

            for ii in range(h):
                line = []
                for jj in range(w):
                    p = bb[ii, jj, 0] - b[ii, jj, 0]
                    line.append(p)
                    dog[ii, jj] = (p, p, p)
                img.append(line)

            octave.append(img)
            misc.imsave('../images/%s/dog/' % (sss) + str(i) + '_' + str(j) + '.jpg', dog)
            
        octaves_.append(octave)

    return octaves_


def create_gaussian_pyramid(img):
    """ 创建4组，每组5层的高斯金字塔

    金字塔最下面一层使用长宽各放大一倍、以0.5为标准差进行高斯模糊的图像
    组间尺度间隔以sqrt(2)倍数递增

    """
    octaves = []
    sigmas = [
        [1.60000, 2.01587, 2.53984, 3.20000, 4.03175, 5.07968],
        [3.20000, 4.03175, 5.07968, 6.40000, 8.06350, 10.1594],
        [6.40000, 8.06350, 10.1594, 12.8000, 16.1270, 20.3187],
        [12.8000, 16.1270, 20.3187, 25.6000, 32.2540, 40.6375]
    ]
    h, w = img.shape[:2]
    
    # 创建第一组
    # 先将原始图片放大两倍
    img = md.zoom_in(img)
    # img.save('../images/Helene/Ethan_gray.png')

    octave = []
    for i in range(6):
        print str(i + 1) + '/6...'
        bimg = md.get_gauss_blur_sci(img, sigmas[0][i])
        misc.imsave('../images/%s/gaussian/0_' % (sss) + str(i) + '.jpg', bimg)
        octave.append(bimg)

    # 第一组加入金字塔
    octaves.append(octave)

    # 循环加入后面3组
    # 每一组的第一层是前一组的倒数第三张隔点采样得到
    for i in range(3):
        octave = []
        img = md.zoom_out(img)

        for j in range(6):
            print str(j + 1) + '/6...'

            if j == 0: # 第一层为前一组导数第三幅图降采样得到
                bimg = md.zoom_out(octaves[i][3])
            else:
                bimg = md.get_gauss_blur_sci(img, sigmas[i + 1][j])

            misc.imsave('../images/%s/gaussian/' % (sss) + str(i + 1) + '_' + str(j) + '.jpg', bimg)
            octave.append(bimg)

        octaves.append(octave)

    return octaves


# core = create_gauss_core(0.6)
# for i in range(len(core)):
#     for j in range(len(core)):
#         print core[i][j],
#     print
# 

img = misc.imread('../images/%s/%s.%s' % (sss, sss, typ))

print 'transform to gray...'
gimg = md.get_gray_2(img)

print 'creating gaussian pyramid...'
pyr_gaussian = create_gaussian_pyramid(gimg)

print 'creating dog pyramid...'
pyr_dog = create_DOG_pyramid(pyr_gaussian)

detect_local_extrema(test.stub_create_DOG_pyramid(sss))

# create_DOG_pyramid(gimg)
# 
# bimg = get_gauss_blur(gimg, 0.6)
# bimg.save('test_4.jpg')
