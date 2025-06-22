# Deep Learning for Real-Time Road Sign Detection and Recognition

*BSc Dissertation Project*

This project implements a real-time traffic sign detection and classification system using the Single Shot MultiBox Detector (SSD) with a MobileNet V2 backbone. It showcases the practical application of deep learning techniques for autonomous driving and advanced driver-assistance systems.

Leveraging TensorFlow’s Python API, the German Traffic Sign Recognition Benchmark (GTSRB) dataset is processed and reduced from 43 to 13 key classes, focusing on the most frequent and relevant road signs for robust model training and evaluation.

📄 **[Full Dissertation Report (PDF)](./Bsc_Dissertation_Traffic_Signs.pdf)**

---

## Overview

- **Model**: SSD MobileNet V2
- **Dataset**: German Traffic Sign Recognition Benchmark (GTSRB) - 13 classes
- **Performance**: ~80% accuracy at >30 FPS
- **Framework**: TensorFlow Object Detection API

## Project Structure

```text
├── Preprocessing/          # Dataset processing scripts
├── Configurations/         # Model configuration files
├── Training.ipynb          # Model training notebook
├── ImageDetection.ipynb    # Image inference notebook
├── Tensorboard.ipynb       # Training visualization
└── BSc_Dissertation_Traffic_Signs.pdf
```

## Key Features

- Real-time detection capable of processing video streams
- Optimized for speed-accuracy trade-off suitable for edge devices
- Comprehensive preprocessing pipeline for GTSRB dataset
- Transfer learning from COCO pre-trained weights

## Results

The SSD MobileNet V2 model achieved optimal performance for real-time applications:

- **Accuracy**: ~80% mAP
- **Speed**: >30 FPS on standard hardware
- **Model Size**: Lightweight architecture suitable for deployment

## Usage

1. Follow the preprocessing instructions in `Preprocessing/README.md`
2. Use the provided Jupyter notebooks for training and inference
3. Access trained models and configurations via the [Google Drive repository](https://drive.google.com/drive/folders/1_YZfCh16viMh7m30xI_waKZYIsWaBfzU?usp=sharing)

---

*This project was developed as part of a BSc dissertation focusing on practical deep learning applications for autonomous vehicle systems.*
