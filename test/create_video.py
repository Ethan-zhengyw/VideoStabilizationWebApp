# -*- coding: utf-8 -*-
import cv2



cap = cv2.VideoCapture("C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/walking/walking2.avi")
out = cv2.VideoWriter(filename="C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/walking/input.avi",
                      fourcc=cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                      fps=cap.get(cv2.CAP_PROP_FPS),
                      frameSize=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))


while not cap.isOpened():
    cap = cv2.VideoCapture("C:/Users/Yiwang/Documents/大四/VideoStabilizationWebApp-master/videos/walking/walking2.avi")
    cv2.waitKey(1000)
    print "Wait for the header"

pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

while True:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        cv2.imshow('video', frame)

        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

        # if 10 < pos_frame < 20:
        out.write(frame)

        print str(pos_frame)+" frames"
    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        print "frame is not ready"
        # It is better to wait for a while for the next frame to be ready
        # cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
        break

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == 200:
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        cap.release()
        out.release()
        break