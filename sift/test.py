# -*- coding: utf-8 -*-
import math
from PIL import Image, ImageFilter


# DOG测试桩
def stub_create_DOG_pyramid():
    octaves = []
    for i in range(4):
        octave = []

        for j in range(5):
            path = '../images/Helene/dog/_' + str(i) + '_' + str(j) + '.jpg'
            octave.append(Image.open(path))

        octaves.append(octave)

    return octaves


def stub_create_gaussian_pyramid():
    """ 高斯金字塔函数测试桩
    """
    octaves = []

    for i in range(4):
        octave = []
        for j in range(6):
            path = '../images/Helene/gaussian/' + str(i) + '_' + str(j) + '.jpg'
            octave.append(Image.open(path))
        octaves.append(octave)

    return octaves
