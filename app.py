from tensorflow import keras
import tensorflow
import matplotlib.pyplot as plt
import cv2
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.utils import load_img, img_to_array
from werkzeug.wrappers import Request, Response

app=Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def pred():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)

