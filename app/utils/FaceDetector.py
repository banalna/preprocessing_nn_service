# -*- coding: utf-8 -*-
import numpy as np
import cv2


class FaceDetector:
    """
    Detect faces on the photos
    """

    def __init__(self, path_to_config):
        # some fix path
        import os
        os.chdir(path_to_config.replace(path_to_config.split('/')[-1], ''))
        self.face_cascade = cv2.CascadeClassifier(path_to_config.split('/')[-1])
        self.last_detection = None

    def detect_faces(self, photo) -> (np.ndarray, np.ndarray):
        """

        :param photo: path to photo or ndarray
        :return: ndarray photo and list of
        """
        if type(photo) == str:
            photo = cv2.imread(photo)

        gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20))
        self.last_detection = self.__cut_faces(photo, faces)

        return self.last_detection

    def __cut_faces(self, photo: np.array, faces: np.array) -> np.array:
        """
        By dots cut faces
        """
        result = list()
        for (x, y, w, h) in faces:
            # cv2.rectangle(photo, (x, y), (x + w, y + h), (255, 0, 0), 2)
            result.append(photo[y:y + h, x:x + w])

        return np.array(result)
