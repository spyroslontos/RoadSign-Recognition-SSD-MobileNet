# Road-Sign-Detection Dataset Processing

The German Traffic Sign Recognition Benchmark Details: http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset
GTSRB Archive Page: https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html

The GTSRB has 43 classes with a wide variance amongst the number of images for each class. By keeping only a certain number of
classes (13) that have enough images the training process is expected to perform sufficiently.

1) You will need:
	- GTSRB_Final_Training_Images.zip https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip
	- GTSRB_Final_Test_Images.zip https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_Images.zip
	- GTSRB_Final_Test_GT.zip https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_GT.zip

2) You will extract all 3 in the same folder
	1) In the 'GTSRB_Final_Training_Images.zip' navigate until you find the 'images' folder and extract that. Then rename the folder to "train"
	2) In the 'GTSRB_Final_Test_Images.zip'navigate until you find the images folder and extract that. Then rename its folder to "eval"
	3) Go in the 'eval' folder, find the 'GT-final_test.test' csv and delete it.
	4) Then in the 'GTSRB_Final_Test_GT.zip' extract the csv in the 'eval' folder.
	5) Additionally, create an empty folder and name it 'test'
	6) When processing the evaluation set 150 randomly chosen images will be extracted in the test folder which can be used to train the performance of your trained model

3) Download all files and put them in your main directory which should contain the 3 folders (train, eval, test)

4) Run the following commands to execute the scripts
	- python label_map_generator.py
	- python eval_test_csv_generator.py
	- python train_csv_generator.py
	- python generate_tfrecord.py --csv_input=train_labels.csv --image_dir=train --output_path=train.record
	- python generate_tfrecord.py --csv_input=eval_labels.csv --image_dir=eval --output_path=eval.record

5) By following the instructions you should have the 2 .record files, the .pbtxt label map, 3 csv files contain annotation information and a test folder holding 150 images.
	These will all be used for training, evaluation and testing purposes
