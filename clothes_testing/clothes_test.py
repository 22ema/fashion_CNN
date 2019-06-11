

#from google.colab import drive
#
#drive.mount('/content/gdrive')
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
from matplotlib import pyplot as plt
import cv2
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("image", type=str,help="image_read")

args = parser.parse_args()
print(args.image) 
print("hello")
# load the image
image_color =  cv2.imread(args.image,cv2.IMREAD_COLOR)
image_ori = cv2.imread(args.image,cv2.IMREAD_GRAYSCALE)
ret, image2=cv2.threshold(image_ori,127,256,cv2.THRESH_BINARY_INV)
image=cv2.bitwise_and(image_ori,image_ori,mask=image2)
orig = image.copy()
 
# pre-process the image for classification
image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

model = load_model('./clothes_train.model')
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
 
new_path = './result_image/'+label
count_i= 0
file_list=list()
for image,_,files in os.walk(new_path):
    file_list = sorted(files)
count_i=len(file_list)+1
count_s=str(count_i)
# show the output image
cv2.imwrite("./result_image/"+label+"/"+count_s+".jpg",image_color)
