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
folderIDList = []
# Gets the 13 class IDs which we will use
with open('labels.csv', 'r') as currentfile:
    reader = csv.reader(currentfile)
    next(reader)
    for row in reader:
        classIDList.append(row[0])
        folderIDList.append(row[0].zfill(5))

os.chdir('train')
parentDirectory = os.getcwd()

# Converting the images to pngs and grouping them in the same folder
# Grouping all of the csvs in the same folder
for folder in os.listdir(os.getcwd()):
    if folder in folderIDList:
        os.chdir(folder)
        # Change the images from .ppm to .png and rename by adding their classId in the beginning
        # (renaming is necessary due to filenames being the same in the different class folders
        for ppmfile in glob.glob('*.ppm'):

            i = cv2.imread(ppmfile)
            os.chdir('..')
            cv2.imwrite(folder+'_'+ppmfile.split('.')[0]+'.png', i)
            os.chdir(folder)
            os.remove(ppmfile)

        # Grouping all of the csvs in the same folder
        for csvfile in glob.glob('*.csv'):
            shutil.move(csvfile, parentDirectory)
            print('Moved: ', csvfile)

        os.chdir('..')
        os.removedirs(folder)
        print('Removed directory: ', folder)


    else:
        shutil.rmtree(folder)
        print('Removed directory: ', folder)

print('Successfully converted ppms to pngs with their class rename')
print('Successfully moved the csvs to their parent directory')
print('Successfully discarded the unwanted classes')

csv_list = []
# Retrieves the information for each image from the csv file
# and stores the image names which we will discard as they are not part of the 13 classes we want
for oldfile in glob.glob('*.csv'):
    with open(oldfile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        next(readCSV)

        for row in readCSV:
            classID = row[7].zfill(5)
            firstPart = row[0].split('.')[0]
            filename = classID + '_' + firstPart + '.png'
            width = row[1]
            height = row[2]
            label = labelMaker(row[7])
            ymin = row[4]
            xmin = row[3]
            ymax = row[6]
            xmax = row[5]

            # print(filename, width, height, label, ymin, xmin, ymax, xmax)
            value = filename, width, height, label, ymin, xmin, ymax, xmax
            csv_list.append(value)

    os.remove(oldfile)

# Shuffle the list
random.shuffle(csv_list)
os.chdir('..')

column_name = ['filename', 'width', 'height', 'class', 'ymin', 'xmin', 'ymax', 'xmax']
csv_df = pd.DataFrame(csv_list, columns=column_name)
csv_df.to_csv('train_labels.csv', index=None)
print('Successfully merged the CSVs and created the train_labels csv')
