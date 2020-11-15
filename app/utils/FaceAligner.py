# -*- coding: utf-8 -*-

import dlib
import numpy as np
import skimage.transform as tr

from app.utils.FaceAlignMask import FaceAlignMask


class FaceAligner:
    """
    dlib_predictor_path: pretrained predictor
    face_template_path: Reference position of key points from dlib
    """

    def __init__(self,
                 dlib_predictor_path="shape_predictor_68_face_landmarks.dat",
                 face_template_path="face_template.npy"):
        # dlib not works with absolute paths
        import os
        os.chdir(dlib_predictor_path.replace(dlib_predictor_path.split('/')[-1], ''))

        self.predictor = dlib.shape_predictor(dlib_predictor_path.split('/')[-1])
        self.face_template = np.load(face_template_path.split('/')[-1])

    def get_landmarks(self,
                      image,
                      face_rect):
        points = self.predictor(image, face_rect)
        return np.array(list(map(lambda p: [p.x, p.y], points.parts())))

    def align_face(self,
                   image,
                   face_rect, *,
                   dim=48,
                   border=0,
                   mask=FaceAlignMask.INNER_EYES_AND_BOTTOM_LIP):
        mask = np.array(mask.value)

        landmarks = self.get_landmarks(image, face_rect)
        proper_landmarks = border + dim * self.face_template[mask]
        A = np.hstack([landmarks[mask], np.ones((3, 1))]).astype(np.float64)
        B = np.hstack([proper_landmarks, np.ones((3, 1))]).astype(np.float64)
        T = np.linalg.solve(A, B).T

        wrapped = tr.warp(image,
                          tr.AffineTransform(T).inverse,
                          output_shape=(dim + 2 * border, dim + 2 * border),
                          order=3,
                          mode='constant',
                          cval=0,
                          clip=True,
                          preserve_range=True)

        return wrapped

    def align_faces(self,
                    image,
                    face_rects,
                    *args,
                    **kwargs):
        result = []

        for rect in face_rects:
            result.append(self.align_face(image, rect, *args, **kwargs))

        return np.array(result).astype(np.uint8)
