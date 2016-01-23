# -*- coding: utf-8 -*-

import cv2
import numpy as np
import module_sift as mds


def make_stable(path_to_input, path_to_output):

    in_video = cv2.VideoCapture(path_to_input)

    if not in_video.isOpened():
        print('Fail to load input video')
        return False

    flag, first_frame = in_video.read()

    out_video = cv2.VideoWriter(filename=path_to_output,
                                fourcc=cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                fps=in_video.get(cv2.CAP_PROP_FPS),
                                frameSize=(first_frame.shape[1], first_frame.shape[0]))

    cur_frame = first_frame
    pos_frame = in_video.get(cv2.CAP_PROP_POS_FRAMES)
    out_video.write(cur_frame)
    while True:

        flag, next_frame = in_video.read()

        if flag:
            pos_frame = in_video.get(cv2.CAP_PROP_POS_FRAMES)
            print('writing frame %d', in_video.get(cv2.CAP_PROP_POS_FRAMES))
            next_frame_adjusted = mds.adjust_frame(cur_frame, next_frame)
            out_video.write(next_frame_adjusted)
            cur_frame = next_frame_adjusted
            # cur_frame = next_frame.copy()
        else:
            # The next frame is not ready, so we try to read it again
            in_video.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
            print "frame is not ready"
            # It is better to wait for a while for the next frame to be ready
            # cv2.waitKey(1000)

        if cv2.waitKey(10) == 27:
            in_video.release()
            out_video.release()
            break

        if in_video.get(cv2.CAP_PROP_POS_FRAMES) == in_video.get(cv2.CAP_PROP_FRAME_COUNT):
            # If the number of captured frames is equal to the total number of frames,
            # we stop
            in_video.release()
            out_video.release()
            break

        if in_video.get(cv2.CAP_PROP_POS_FRAMES) == 200:
            # If the number of captured frames is equal to the total number of frames,
            # we stop
            in_video.release()
            out_video.release()
            break



make_stable('C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/mingde/input3.avi',
            'C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/mingde/out15.avi')