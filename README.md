# Action_Recognition_3D_CNN

### Description
This is a code for implementation of 3D Convolutional Neural Network for video classification using Keras(tensorflow backend).

### Requirements
* Python 3.7 (Anaconda)
* Opencv 4.1.0
* Keras 2.2.4
* Tensorflow 1.14
* CUDA 10.1

### Dataset
UCF-101 Dataset : [Click here](https://www.crcv.ucf.edu/data/UCF101.php)

### Dataset Setup
First we need to move all the videos in a folder UCF101
```
python move_videos.py
```
### Model Architecture

### To run the code
```
python 3dcnn.py --batch 32 --epoch 50 --videos /home/ayush/Activity_Recognition/3DCNN/UCF101/ --nclass 10 --output 3dcnnresult/ --color True --skip False --depth 15
```

### Some Experimental Results

#### Experiment 1
* Num Classes : 101
* Epochs : 100
![Loss Plot](https://github.com/rayush7/Action_Recognition_3D_CNN/blob/master/test3_3dcnnresult_101/model_loss.png)
![Accuracy Plot](https://github.com/rayush7/Action_Recognition_3D_CNN/blob/master/test3_3dcnnresult_101/model_accuracy.png)

#### Experiment 2
* Num Classes : 50
* Epochs : 100
![Loss Plot](https://github.com/rayush7/Action_Recognition_3D_CNN/blob/master/test2_3dcnnresult_50/model_loss.png)
![Accuracy Plot](https://github.com/rayush7/Action_Recognition_3D_CNN/blob/master/test2_3dcnnresult_50/model_accuracy.png)


#### Experiment 3
* Num Classes : 10
* Num Epochs : 100
![Loss Plot](https://github.com/rayush7/Action_Recognition_3D_CNN/blob/master/test1_3dcnnresult_10/model_loss.png)
![Accuracy Plot](https://github.com/rayush7/Action_Recognition_3D_CNN/blob/master/test1_3dcnnresult_10/model_accuracy.png)

### Credits
* [kcct-fujimotolab Github Repository](https://github.com/kcct-fujimotolab/3DCNN)

