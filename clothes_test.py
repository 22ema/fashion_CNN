# -*- coding: utf-8 -*-
"""clothes_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fVSzY6kLHM3zgM-BG2oYlSzdRiRxdjef
"""

from google.colab import drive

drive.mount('/content/gdrive')
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
from matplotlib import pyplot as plt
import cv2
# load the image
image = cv2.imread('/content/gdrive/My Drive/test_data/t.jpg',cv2.IMREAD_GRAYSCALE)
ret, image2=cv2.threshold(image,127,256,cv2.THRESH_BINARY_INV)
image=cv2.bitwise_and(image,image,mask=image2)
cv2.imwrite("content/gdrive/My Drive/test_data/good.jpg",image)
print(image)
plt.imshow(image)
plt.show()
orig = image.copy()
 
# pre-process the image for classification
image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

model = load_model('/content/gdrive/My Drive/clothes_train.model')
clo_list=dict()
# classify the input image
(t_shirt,trouser,pullover,dress,coat,sandal,shirt,sneaker,bag,ankleboot) = model.predict(image)[0]
clo_list= {"t_shirt":t_shirt,"trouser":trouser,"pullover":pullover,"dress":dress,"coat":coat,"sandal":sandal,"shirt":shirt,"sneaker":sneaker,"bag":bag,"ankleboot":ankleboot}
print(clo_list)
def call_(x):
    return clo_list[x]
key_max = max(clo_list.keys(), key=call_)

print(key_max)

# build the label
label = key_max
proba = clo_list[key_max]
label = "{}: {:.2f}%".format(label, proba * 100)
 
# draw the label on the image
output = imutils.resize(orig, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)
 
# show the output image
plt.imshow(output)
plt.show()