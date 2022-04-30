# Hand_Gesture_Recognition

*Libraries Rerquired:*

import mediapipe as mp

from math import hypot

import screen_brightness_control

import numpy as np

import cv2








__Issues:__

1) https://github.com/TheCleverIdiott/Hand_Gesture_Recognition/blob/main/Bare_Minimum_Module.py 
showing the following error:

" Traceback (most recent call last):
  File "c:\Users\User\Desktop\HandTrackingModule.py", line 55, in <module>
    main()
  File "c:\Users\User\Desktop\HandTrackingModule.py", line 37, in main
    detector = handDetector()
  File "c:\Users\User\Desktop\HandTrackingModule.py", line 15, in _init_
    self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
  File "C:\Users\User\AppData\Local\Programs\Python\Python310\lib\site-packages\mediapipe\python\solutions\hands.py", line 114, in _init_
    super()._init_(
  File "C:\Users\User\AppData\Local\Programs\Python\Python310\lib\site-packages\mediapipe\python\solution_base.py", line 258, in _init_
    self._input_side_packets = {
  File "C:\Users\User\AppData\Local\Programs\Python\Python310\lib\site-packages\mediapipe\python\solution_base.py", line 259, in <dictcomp>
    name: self._make_packet(self._side_input_type_info[name], data)
  File "C:\Users\User\AppData\Local\Programs\Python\Python310\lib\site-packages\mediapipe\python\solution_base.py", line 513, in _make_packet
    return getattr(packet_creator, 'create_' + packet_data_type.value)(data)
TypeError: create_int(): incompatible function arguments. The following argument types are supported:
    1. (arg0: int) -> mediapipe.python._framework_bindings.packet.Packet

Invoked with: 0.5
[ WARN:0@5.213] global D:\a\opencv-python\opencv-python\opencv\modules\videoio\src\cap_msmf.cpp (539) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback"


