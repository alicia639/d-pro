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
  bl_h, bl_w = 64, 64

  for row in np.arange(im_h - bl_h + 1, step=bl_h):
    for col in np.arange(im_w - bl_w + 1, step=bl_w):
      img = np_image[row:row+bl_h, col:col+bl_w]
      img = transform.resize(img, (64, 64, 3))
      img = np.expand_dims(img, axis=0)
      pred = model.predict(img)
      result = np.argmax(pred, axis =1)
      if result == 0:
        return "Bad"

  return "Good"

  #add in neither... if confidence less than certain value, ignore
