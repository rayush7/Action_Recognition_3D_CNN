# Action_Recognition_3D_CNN

# Description
This is a code for implementation of 3D Convolutional Neural Network for video classification using Keras(tensorflow backend).

# Requirements
* Python 3.7 (Anaconda)
* Opencv 4.1.0
* Keras 2.2.4
* Tensorflow 1.14
* CUDA 10.1

# Dataset
UCF-101 Dataset : [Click here](https://www.crcv.ucf.edu/data/UCF101.php)

# Dataset Organisation
First we need to move videos
```
python move_videos.py
```
# Model Architecture

# To run the code
```
python 3dcnn.py --batch 32 --epoch 50 --videos /home/ayush/Activity_Recognition/3DCNN/UCF101/ --nclass 10 --output 3dcnnresult/ --color True --skip False --depth 15
```

# Some Experimental Results


# Credits
* [Github Repository](https://github.com/eriklindernoren/Action-Recognition)

