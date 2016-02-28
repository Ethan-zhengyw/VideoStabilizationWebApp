# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np
import module_sift as mds


def make_stable(path_to_input):
    dir_path = path_to_input[:path_to_input.rfind('/') + 1]
    path_to_output = dir_path + 'video_stabled.avi'

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

    print('making %s stable into %s...' % (path_to_input, path_to_output))
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

        if in_video.get(cv2.CAP_PROP_POS_FRAMES) == 5:
            # If the number of captured frames is equal to the total number of frames,
            # we stop
            in_video.release()
            out_video.release()
            break

    return path_to_output


def split2audio_video(path_to_input):
    dir_path = path_to_input[:path_to_input.rfind('/') + 1]

    path_to_audio = dir_path + 'sound.mp3'
    path_to_video = dir_path + 'video.avi'

    extract_audio = r'..\ffmpeg\bin\ffmpeg.exe -i %s -vn -ar' \
                    r' 44100 -ac 2 -ab 192k -f mp3 %s -y' % (path_to_input, path_to_audio)
    extract_video = r'..\ffmpeg\bin\ffmpeg.exe -i %s -map 0:1  -vcodec mjpeg %s -y' % (path_to_input, path_to_video)

    print('extracting audio from %s to %s...' % (path_to_input, path_to_audio))
    os.system(extract_audio)
    print('extracting video from %s to %s...' % (path_to_input, path_to_video))
    os.system(extract_video)

    return path_to_audio, path_to_video


def combine_audio_video(path_to_audio, path_to_stabled):
    dir_path = path_to_audio[:path_to_audio.rfind('/') + 1]

    path_to_audio = dir_path + 'sound.mp3'
    path_to_result = dir_path + 'result.mp4'

    extract_combination = r'..\ffmpeg\bin\ffmpeg.exe -i %s -i %s -c:v h264 -c:a copy %s -y'\
                          % (path_to_stabled, path_to_audio, path_to_result)

    print('combining %s and %s to %s...' % (path_to_audio, path_to_stabled, path_to_result))
    os.system(extract_combination)


def process(path_to_input):
    audio, video = split2audio_video(path_to_input)
    stabled = make_stable(video)
    combine_audio_video(audio, stabled)

    # 删除中间文件
    del_mid_file = 'del %s %s %s' % (audio.replace('/', '\\'), video.replace('/', '\\'), stabled.replace('/', '\\'))

    print('deleting middle file...')
    os.system(del_mid_file)

process('../videos/gogo/gogo.mp4')
