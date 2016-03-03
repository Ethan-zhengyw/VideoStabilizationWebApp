# -*- coding: utf-8 -*-
import math
from PIL import Image, ImageFilter
from scipy import misc


# DOG测试桩
def stub_create_DOG_pyramid(sss):
    octaves = []
    for i in range(4):
        octave = []

        for j in range(5):
            path = '../images/%s/dog/' % (sss) + str(i) + '_' + str(j) + '.jpg'
            octave.append(misc.imread(path))

        octaves.append(octave)

    return octaves


def stub_create_gaussian_pyramid(sss):
    """ 高斯金字塔函数测试桩
    """
    octaves = []

    for i in range(4):
        octave = []
        for j in range(6):
            path = '../images/%s/gaussian/' % (sss) + str(i) + '_' + str(j) + '.jpg'
            octave.append(misc.imread(path))
        octaves.append(octave)

    return octaves
