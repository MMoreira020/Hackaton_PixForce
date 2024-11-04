# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Tx5W0rOHHb620eIuSKQWEMPGUm3zkOc
"""

!pip install ultralytics
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="eTh8t6xOiHzPDHnx9ikA")
project = rf.workspace("roboflow-jvuqo").project("football-players-detection-3zvbc")
version = project.version(1)
dataset = version.download("yolov5")

dataset.location

import shutil

shutil.move("football-players-detection-1/train",
            "football-players-detection-1/football-players-detection-1/train"
            )

shutil.move("football-players-detection-1/test",
            "football-players-detection-1/football-players-detection-1/test"
            )

shutil.move("football-players-detection-1/valid",
            "football-players-detection-1/football-players-detection-1/valid"
            )

!yolo task=detect mode=train model=yolov5l.pt data={dataset.location}/data.yaml epochs=50 imgsz=640
