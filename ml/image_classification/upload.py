from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import os

from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import efficientnet.tfkeras as efn
import tensorflow.keras.layers as L
from tensorflow.keras.models import Model

# building the complete model
model = load_model('./best_model.h5')

from PIL import Image
import numpy as np
from skimage import transform
import matplotlib.pyplot as plt

def pred(filename):
  np_image = Image.open(filename)
  np_image = np.array(np_image).astype('float32')/255

  im_h, im_w = np_image.shape[:2]
  sq = 64


  for row in range(0, im_h-sq-1):
    for col in range(0, im_w-sq-1):
      #print(row)
      #print(col)
      img = np_image[row:row+sq, col:col+sq]
      img = transform.resize(img, (64, 64, 3))
      img = np.expand_dims(img, axis=0)
      pred = model.predict(img)
      #print(pred)
      result = np.argmax(pred, axis=1)
      #print(result)
      if result == 0 and pred > 0.5:
        #print(np.average(np.mean(img, axis=(0, 1))))
        if (np.average(np.mean(img, axis=(0, 1)))) <  0.3:
            return "Bad"

  return "Good"
