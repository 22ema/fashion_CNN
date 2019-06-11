# fashion_CNN
We want new application to use this convolution neural network.

## explain
 - clothes_test.py
 - clothes_train.py
 - mnist file
 
 fashion mnist를 이용해서 옷과 그밖의 것들을 학습하는 cnn이다. train을 통해서 학습하고 test를 통해서 test한다.

 자신의 데이터로 테스트를 하고싶다면 이진화를 하고 하는 것을 추천한다. 위의 test 코드에 포함 되어있으니 확인 해보길 바란다.
 추가적으로 csv파일을 kaggle 가서 들고와서 해보길 바란다.


 - reference : https://www.kaggle.com/bugraokcu/cnn-with-keras/notebook
 - https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/

 ## update 2019-06-11
 
 - clothes_testing

 #### -- kr

 쉘 스크립트를 이용하여 rinux 환경에서 리눅스 부팅과 동시에 이미지를 분류하는 코드를 실행시킨다.
 이때 새로운 이미지 파일이 들어오는지를 정해준 시간마다 확인하여 새로운 파일이 들어오면 다시 코드를 실행하는 방향으로 구현하였다.
 아쉽게도 현재 프로그램은 background에서 무한루프형태로 돌아가고 있어서 성능이 좋지 아니하다. 차후 개선필요
 
 #### -- en

 Run the code that classifies the image at the same time as the Linux boot in the rinux environment using a shell script.
 
 At this time, it was implemented in a way to check if a new image file was coming in every specified time and to execute the code again when a new file came in.
 
 Unfortunately, the current program is returning from the background to the infinity loop, and performance is not good. Need to improve later
 
 

