import cv2
import time
#from tflite_support.task import core
#from tflite_support.task import processor
import mediapipe as mp
import utils
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


model='efficientdet_lite0.tflite'
num_threads=4

cap = cv2.VideoCapture(0)
base_options = python.BaseOptions(file_name=model, use_coral=False,num_threads=num_threads)
options= vision.ObjectDetectorOptions(
    base_options=base_options,
    score_threshold=0.3,
    max_results=8
)
detector=