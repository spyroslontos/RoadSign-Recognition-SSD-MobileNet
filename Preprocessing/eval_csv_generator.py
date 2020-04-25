import os
import shutil
import random
import csv
import glob
import cv2
import pandas as pd

# changes from classId to the name of the label
def labelMaker(classId):
    if classId == '1':
        return 'Speed limit (30km/h)'
    if classId == '2':
        return 'Speed limit (50km/h)'
    if classId == '3':
        return 'Speed limit (60km/h)'
    if classId == '4':
        return 'Speed limit (70km/h)'
    if classId == '5':
        return 'Speed limit (80km/h)'
    if classId == '7':
        return 'Speed limit (100km/h)'
    if classId == '8':
        return 'Speed limit (120km/h)'
    if classId == '9':
        return 'No passing'
    if classId == '10':
        return 'No passing for vehicles over 3.5 metric tons'
    if classId == '12':
        return 'Priority road'
    if classId == '13':
        return 'Yield'
    if classId == '25':
        return 'Road work'
    if classId == '38':
        return 'Keep right'

classIDList = []
# Gets the 13 class IDs which we will use
with open('labels.csv', 'r') as currentfile:
    reader = csv.reader(currentfile)
    next(reader)
    for row in reader:
        classIDList.append(row[0])

parentDirectory = os.getcwd()
os.chdir('eval')

csv_list = []
discardedImagesList = []
# Retrieves the information for each image from the csv file
# and stores the image names which we will discard as they are not part of the 13 classes we want
with open('GT-final_test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    next(readCSV)

    for row in readCSV:
        if row[7] in classIDList:

            firstPart = row[0].split('.')[0]
            filename = firstPart + '.png'
            width = row[1]
            height = row[2]
            label = labelMaker(row[7])
            ymin = row[4]
            xmin = row[3]
            ymax = row[6]
            xmax = row[5]

            # print(filename, width, height, label, ymin, xmin, ymax, xmax)

            # Store each line in a list
            value = filename, width, height, label, ymin, xmin, ymax, xmax
            csv_list.append(value)

        else:
            filename = row[0]
            discardedImagesList.append(filename)

# Removes the discarded images
for image in discardedImagesList:
    os.remove(image)

# Change the images from .ppm to .png
for ppmfile in glob.glob('*.ppm'):

    i = cv2.imread(ppmfile)
    cv2.imwrite(ppmfile.split('.')[0]+'.png', i)
    os.remove(ppmfile)

print('Successfully converted ppms to pngs')

# Shuffle the list to improve evaluation/training
random.shuffle(csv_list)

# Randomly picks 50 images and moves them to the test folder
# These images will not be used in training
destination = os.path.join(parentDirectory, 'test')
for i in range(50):
    choice = random.choice(csv_list)
    shutil.move(choice[0], destination)
    csv_list.remove(choice)

# Removes the csv file that we will not need
os.remove('GT-final_test.csv')
os.chdir('..')

column_name = ['filename', 'width', 'height', 'class', 'ymin', 'xmin', 'ymax', 'xmax']
csv_df = pd.DataFrame(csv_list, columns=column_name)
csv_df.to_csv('eval_labels.csv', index=None)
print('Successfully created the eval_labels csv')
