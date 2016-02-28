# -*- coding: utf-8 -*-
import cv2
import os

def convert2avi(path_to_input):
    print('converting %s' % path_to_input)
    in_video = cv2.VideoCapture(path_to_input)

    if not in_video.isOpened():
        print('Fail to load input video.')

    else:
        print('Load input video down.')

    # print('converting to avi...')
    # os.system(r'..\ffmpeg\bin\ffmpeg.exe -i ' + path_to_input + ' ' + path_to_input[:path_to_input.rfind('.')] + '2.avi')

convert2avi('../videos/gogo/video.avi')
# convert2avi('C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/mingde/input.avi')
# convert2avi(unicode('C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/mingde/input.avi', "utf8").encode('gbk'))