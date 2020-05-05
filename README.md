# CM3203-Road-Sign-Detection-Code

Dissertation Version Control for Road Sign Detection and Recognition using deep learning Techniques

Four Google Colab notebooks which can be used for training, evaluation and testing for both video and image detection.

'Preprocessing' contains steps, python scripts and a labels csv file that can be used to process the German Traffic Sign Recognition Benchmark (GTSRB) Dataset. It does not use all 43 classes found within GTSRB but is instead trimmed to just 13 classes. These 13 classes are the ones containing the higest number of training and evaluation images.

'Configurations' has 2 configuration files which can be used with their corresponding pre-trained models as well as the model_main.py with some minor changes on the number of loggins steps and the checkpoint saving intervals
