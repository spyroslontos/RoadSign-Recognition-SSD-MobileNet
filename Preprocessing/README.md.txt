# CM3203-Road-Sign-Detection-Code

Dissertation Version Control for Road Sign Detection and Recognition

Preprocessing contains the pre-processing steps to create the tf records used for training and evaluation. It does not use all 43 classes found withing the German Traffic Sign Database (GTSDB) but instead trimmed to just 13 classes. These 13 classes are the ones containing the most individual training and evaluation images. This results in more accurate training results and creates a more generalized model.
