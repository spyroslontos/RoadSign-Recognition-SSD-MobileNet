import os
import shutil
import random
import csv
import glob
import cv2
import pandas as pd


# changes from classId to the name of the label
def labelMaker(classId):
    if classId == '0':
        return 'Speed limit (20km/h)'
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
    if classId == '6':
        return 'End of speed limit (80km/h)'
    if classId == '7':
        return 'Speed limit (100km/h)'
    if classId == '8':
        return 'Speed limit (120km/h)'
    if classId == '9':
        return 'No passing'
    if classId == '10':
        return 'No passing for vehicles over 3.5 metric tons'
    if classId == '11':
        return 'Right-of-way at the next intersection'
    if classId == '12':
        return 'Priority road'
    if classId == '13':
        return 'Yield'
    if classId == '14':
        return 'Stop'
    if classId == '15':
        return 'No vehicles'
    if classId == '16':
        return 'Vehicles over 3.5 metric tons prohibited'
    if classId == '17':
        return 'No entry'
    if classId == '18':
        return 'General caution'
    if classId == '19':
        return 'Dangerous curve to the left'
    if classId == '20':
        return 'Dangerous curve to the right'
    if classId == '21':
        return 'Double curve'
    if classId == '22':
        return 'Bumpy road'
    if classId == '23':
        return 'Slippery road'
    if classId == '24':
        return 'Road narrows on the right'
    if classId == '25':
        return 'Road work'
    if classId == '26':
        return 'Traffic signals'
    if classId == '27':
        return 'Pedestrians'
    if classId == '28':
        return 'Children crossing'
    if classId == '29':
        return 'Bicycles crossing'
    if classId == '30':
        return 'Beware of ice/snow'
    if classId == '31':
        return 'Wild animals crossing'
    if classId == '32':
        return 'End of all speed and passing limits'
    if classId == '33':
        return 'Turn right ahead'
    if classId == '34':
        return 'Turn left ahead'
    if classId == '35':
        return 'Ahead only'
    if classId == '36':
        return 'Go straight or right'
    if classId == '37':
        return 'Go straight or left'
    if classId == '38':
        return 'Keep right'
    if classId == '39':
        return 'Keep left'
    if classId == '40':
        return 'Roundabout mandatory'
    if classId == '41':
        return 'End of no passing'
    if classId == '42':
        return 'End of no passing by vehicles over 3.5 metric tons'


os.chdir('train')
parentDirectory = os.getcwd()

# Converting the images to pngs and grouping them in the same folder
# Grouping all of the csvs in the same folder
for folder in os.listdir(os.getcwd()):
    os.chdir(folder)

    # Change the images from .ppm to .png and rename by adding their classId in the beginning
    # (renaming is necessary due to filenames being the same in the different class folders
    for ppmfile in glob.glob('*.ppm'):

        i = cv2.imread(ppmfile)
        os.chdir('..')
        cv2.imwrite(str(int(folder)+1)+'_'+ppmfile.split('.')[0]+'.png', i)
        os.chdir(folder)
        os.remove(ppmfile)

    # Grouping all of the csvs in the same folder
    for csvfile in glob.glob('*.csv'):
        print(csvfile)
        shutil.move(csvfile, parentDirectory)

    os.chdir('..')
    print('Removed directory: ', end='')
    os.removedirs(folder)

print('Successfully converted ppms to pngs with their class rename')
print('Successfully moved the csvs to their parent directory')

csv_list = []
for oldfile in glob.glob('*.csv'):
    with open(oldfile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        next(readCSV)
        # print(oldfile)

        for row in readCSV:
            classID = int(row[7])+1
            firstPart = row[0].split('.')[0]
            filename = str(classID) + '_' + firstPart + '.png'
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

# Shuffle the list to improve testing/training
random.shuffle(csv_list)

os.chdir('..')

column_name = ['filename', 'width', 'height', 'class', 'ymin', 'xmin', 'ymax', 'xmax']
csv_df = pd.DataFrame(csv_list, columns=column_name)
csv_df.to_csv('train_labels.csv', index=None)
print('Successfully merged the CSVs and created the train_labels csv')
