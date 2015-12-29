#-*- coding: utf-8 -*-

""" Module of basic functions to process image
"""

import math
from PIL import Image, ImageFilter

def gaussian(sigma, x, y):
    return math.exp(-1.0 * (x*x + y*y) / (2 * sigma * sigma)) \
            / (2.0 * math.pi * sigma * sigma)


# 把图片放大两倍, 每个像素延伸为原来的四倍
def zoom_in(img):
    h = img.size[0] * 2
    w = img.size[1] * 2

    img_ = Image.new('RGB', (h, w), (0, 0, 0))
    for i in range(h):
        for j in range(w):
            img_.putpixel((i, j), img.getpixel((i / 2, j / 2)))

    return img_


# 对图像进行降采样，使其分辨率减半
def zoom_out(img):
    h = img.size[0] / 2
    w = img.size[1] / 2

    img_ = Image.new('RGB', (h, w), (0, 0, 0))

    for i in range(h):
        for j in range(w):
            img_.putpixel((i, j), img.getpixel((i * 2, j * 2)))

    return img_


def get_gauss_blur(img, sigma):
    """ 标准高斯模糊函数

    :param img: 原图像
    :param sigma: 高斯分布标准差

    """
    img_blur = Image.new('RGB', img.size, (0, 0, 0))

    # 根据标准差创建高斯模板
    gauss_core = create_gauss_core(sigma)

    r = (int)((len(gauss_core) - 1) / 2)

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # print str(i*img.size[0] + img.size[1]) + '/' + str(img.size[0] * img.size[1]) + '...'
            acc = 0
            for h in range(-r, r + 1, 1):
                for w in range(-r, r + 1, 1):
                    ii, jj = i + h, j + w
                    if ii >= 0 and ii < img.size[0] and jj >= 0 and jj < img.size[1]:
                        acc += img.getpixel((ii, jj))[0] * gauss_core[r + h][r + w]
            acc = (int)(acc)
            img_blur.putpixel((i, j), (acc, acc, acc))

    return img_blur


def get_gray_1(img):
    """ 通过RGB三个通道的平均值计算灰度图

    :param img: Image对象，通过PIL.Image.open('filename.xxx')得到

    """

    img_gray = Image.new('RGB', img.size, (0, 0, 0))

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = img.getpixel((i, j))
            avg = (pixel[0] + pixel[1] + pixel[2]) / 3
            img_gray.putpixel((i, j), (avg, avg, avg))

    return img_gray



def get_gray_2(img):
    """ 对于彩色转灰度，有一个很著名的心理学公式：

            Gray = R*0.299 + G*0.587 + B*0.114

        移位代替除法：

            Gray = (R*38 + G*75 + B*15) >> 7

    :param img: Image对象，通过PIL.Image.open('filename.xxx')得到

    """

    img_gray = Image.new('RGB', img.size, (0, 0, 0))

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixel = img.getpixel((i, j))
            res = (pixel[0] * 38 + pixel[1] * 75 + pixel[2] * 15) >> 7
            img_gray.putpixel((i, j), (res, res, res))

    return img_gray
