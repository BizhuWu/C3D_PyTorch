# C3D_PyTorch
This project includes the whole training process. Specifically, I use PyTorch 1.7 **`VideoIO / Video Datasets Loading API / Video Transform`** to process the Data. [More Details：How to use Video Datasets，Video IO，Video Classification Models，Video Transform in PyTorch](https://blog.csdn.net/qq_36627158/article/details/113791050)

The C3D's paper：Learning Spatiotemporal Features with 3D Convolutional Networks. [download](https://arxiv.org/pdf/1412.0767.pdf)

The C3D model's definition code refers to [jfzhang95](https://github.com/jfzhang95/pytorch-video-recognition/blob/master/network/C3D_model.py)

&nbsp;


## Performance
Accuracy     | 
:-----------:|
-- Still Training Now --  |

&nbsp;


## Training Environment
+ Ubuntu 16.04.7 LTS
+ CUDA Version: 10.1
+ PyTorch 1.7.1
+ torchvision 0.8.2
+ numpy 1.19.2
+ pillow 8.1.0
+ python 3.8.5
+ av 8.0.3
+ matplotlib 3.3.4

&nbsp;

## Data Preparation
Original Dataset：[UCF101](https://www.crcv.ucf.edu/data/UCF101.php)

After downloading the UCF101 dataset: **`UCF101.rar`** and **`UCF101TrainTestSplits-RecognitionTask.zip`**, you should seperately unrar them. Then put it into the directory named **`data`**
```
Project
│--- data
│------ UCF101
│------ UCF101TrainTestSplits-RecognitionTask
│--- other files
```

&nbsp;

## Train
Before training, make sure you have a directory named **`model`** in the root project to save checkpoint file.
```python
python3 train.py
```
&nbsp;

## Problems
I recorded some problems and solutions when writing the code. Really so sorry that I only write in Chinese! 
Here is the [Link](https://blog.csdn.net/qq_36627158/article/details/113914626)
