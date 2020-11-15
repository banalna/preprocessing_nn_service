# -*- coding: utf-8 -*-

import numpy as np
import json
import cv2

from flask import current_app, request

from app.utils.NumpyEncoder import NumpyEncoder
from app.utils.FaceDetector import FaceDetector
from app.utils.FaceAligner import FaceAligner

detector = FaceDetector()
aligner = None


def preprocessing_photo():
    global aligner

    if request.method == 'POST':
        if 'file' not in request.files:
            return 400, 'No file part'

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 400, 'No selected file'

        if file and allowed_file(file.filename):
            if not aligner:
                aligner = FaceAligner(current_app.config['DBLIB_PREDICTOR'],
                                      current_app.config['FACE_TEMPLATE_PATH'])
            try:
                image_bytes = file.stream.read()
                decoded_image = rgb_bgr(cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1), True)
                if decoded_image.shape != 3:
                    decoded_image = decoded_image[:, :, :3]

                try:
                    face_rects = detector.detect_faces(decoded_image)
                    faces = cut_faces(decoded_image, face_rects)
                    resized = aligner.align_faces(decoded_image, face_rects)
                    del image_bytes, decoded_image
                except Exception as e:
                    return {'faces': 'not recognition', 'resized': 0, 'error': str(e)}

                json_dump = json.dumps({'faces': faces, 'resized': resized}, cls=NumpyEncoder)
                return json_dump
            except Exception as e:
                print(e)
                return 400, 'Photo not uploaded error: ' + str(e)

    return 400, 'Unhandled error'


def cut_faces(image, face_rects):
    faces = []
    for face_rect in face_rects:
        faces.append(image[face_rect.top():face_rect.bottom(),
                     face_rect.left():face_rect.right()])
    return faces


def rgb_bgr(img, to_rgb=False):
    if to_rgb:
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else:
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


def resize_image(img):
    return cv2.resize(img, (48, 48), interpolation=cv2.INTER_AREA)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS_PHOTO']
