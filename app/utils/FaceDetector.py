# -*- coding: utf-8 -*-
import dlib

import numpy as np
import skimage.transform as tr

from enum import Enum


class FaceDetectorException(Exception):
    pass


class FaceDetector:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def detect_faces(self,
                     image, *,
                     upscale_factor=1,
                     greater_than=None,
                     get_top=None):
        try:
            face_rects = list(self.detector(image, upscale_factor))
        except Exception as e:
            raise FaceDetectorException(e.args)

        if greater_than is not None:
            face_rects = list(filter(lambda r:
                                     r.height() > greater_than and r.width() > greater_than,
                                     face_rects))

        face_rects.sort(key=lambda r: r.width() * r.height(), reverse=True)

        if get_top is not None:
            face_rects = face_rects[:get_top]

        return face_rects
