# Road-Sign-Detection Dataset Processing

1) The german traffic sign dataset and its description can be found here http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset
2) Its download page is here https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html

The GTSDB had 43 classes. Since the number of images in the training set and evaluation set for each class varies. We will keep only a certain number of
classes (13) that can have enough images for the training process to perform sufficiently.

3) We will need 
	- GTSRB_Final_Training_Images.zip https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip
	- GTSRB_Final_Test_Images.zip https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_Images.zip
	- GTSRB_Final_Test_GT.zip https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_GT.zip

4) you will extract all 3 in the same folder that you should call 'dataset'
	1) In the 'GTSRB_Final_Training_Images.zip' navigate until you find the 'images' folder and extract that. Then rename the folder to "train"
	2) In the 'GTSRB_Final_Test_Images.zip'navigate until you find the images folder and extract that. Then rename its folder to "eval"
	3) Go in the 'eval' folder, find the 'GT-final_test.test' csv and delete it.
	4) Then in the 'GTSRB_Final_Test_GT.zip' extract the csv in the 'eval' folder.
	5) Additionally, create an empty folder and name it 'test'
	6) When we will create the eval csv and modify the images we will pick 50 random images and extract them in the test folder to test our trained model

5) Download the 5 python scripts and the labels csv. Add them to the same folder you have added the 'eval' / 'train' images
	- labels.csv
	- train_csv_generator.py
	- eval_test_csv_generator.py
	- generate_tfrecord.py
	- label_map_generator.py
	- test_set_modifier

6) Run the following commands to execute the scripts
	- python label_map_generator.py
	- python eval_test_csv_generator.py
	- python train_csv_generator.py
	- python generate_tfrecord.py --csv_input=train_labels.csv --image_dir=train --output_path=train.record
	- python generate_tfrecord.py --csv_input=eval_labels.csv --image_dir=eval --output_path=eval.record

7) By following the instructions you should have the 2 .record files, the .pbtxt label map and a test folder holding 150 images that we can test on.
	These will all be used for training and evaluation purposes
