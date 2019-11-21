# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:38:42 2019

@author: Gayatri
"""

from imageai.Detection.Custom import DetectionModelTrainer
import os
os.chdir('F:\Internship_CV\ImageAI_Model')

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory='hololens')
trainer.setTrainConfig(object_names_array=['hololens'],batch_size=4,num_experiments=20,train_from_pretrained_model='pretrained-yolov3.h5')
trainer.trainModel()
