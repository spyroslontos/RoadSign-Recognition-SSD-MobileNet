# Dataset Preprocessing

Processing pipeline for the German Traffic Sign Recognition Benchmark (GTSRB) dataset.

## Dataset

- **Source**: [GTSRB Benchmark](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset)
- **Classes**: 43 → 13 (most frequent and well-represented signs)
- **Format**: Images with CSV annotations

## Setup

### 1. Download Required Files

- `GTSRB_Final_Training_Images.zip`
- `GTSRB_Final_Test_Images.zip` 
- `GTSRB_Final_Test_GT.zip`

### 2. Extract and Organize

```text
main_directory/
├── train/          # Training images
├── eval/           # Evaluation images + GT-final_test.test.csv
└── test/           # Empty folder (150 random images will be added)
```

**Steps:**

1. Extract `images/` folder from `GTSRB_Final_Training_Images.zip` → rename to `train/`
2. Extract `images/` folder from `GTSRB_Final_Test_Images.zip` → rename to `eval/`
3. Delete `GT-final_test.test` CSV file from `eval/` folder
4. Extract CSV from `GTSRB_Final_Test_GT.zip` into `eval/` folder
5. Create empty folder named `test/`
6. *Note: During processing, 150 randomly chosen images will be extracted to the `test/` folder for model performance evaluation*

## Processing

Run scripts in order:

```bash
python label_map_generator.py
python eval_test_csv_generator.py
python train_csv_generator.py
python generate_tfrecord.py --csv_input=train_labels.csv --image_dir=train --output_path=train.record
python generate_tfrecord.py --csv_input=eval_labels.csv --image_dir=eval --output_path=eval.record
```

## Output

- `train.record` & `eval.record` - TFRecord files for training
- `label_map.pbtxt` - Label mapping
- CSV annotation files
- `test/` folder with 150 random evaluation images
