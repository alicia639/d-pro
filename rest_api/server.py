from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import numpy as np
from PIL import Image
import numpy as np
from skimage import transform
import matplotlib.pyplot as plt\
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import base64

app = Flask(__name__)
api = Api(app)

class Photo(Resource):

    def get(self, json_image):

        img_string = json_image["img"]

        imgdata = base64.b64decode(str(img_string))

        model = load_model('./best_model.h5')

        np_image = Image.open(io.BytesIO(imgdata))
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
                    return {"val": 0}

        return {"val": 1}

api.add_resource(Photo, '/photos') # Route_1

if __name__ == '__main__':
     app.run(port='5002')
