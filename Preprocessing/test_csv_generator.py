import os
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
        return 'No passing for vechiles over 3.5 metric tons'
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
        return 'End of no passing by vechiles over 3.5 metric tons'


os.chdir('test')

csv_list = []
with open('GT-final_test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    next(readCSV)

    for row in readCSV:
        firstPart = row[0].split('.')[0]
        filename = firstPart + '.png'
        width = row[1]
        height = row[2]
        label = labelMaker(row[7])
        xmin = row[3]
        ymin = row[4]
        xmax = row[5]
        ymax = row[6]

        # print(filename, width, height, label, xmin, ymin, xmax, ymax)

        # Store each line in a list
        value = filename, width, height, label, xmin, ymin, xmax, ymax
        csv_list.append(value)

# Shuffle the list to improve testing/training
random.shuffle(csv_list)


# Change the images from .ppm to .png
for ppmfile in glob.glob('*.ppm'):

    i = cv2.imread(ppmfile)
    cv2.imwrite(ppmfile.split('.')[0]+'.png', i)
    os.remove(ppmfile)

print('Successfully converted ppms to pngs')

# Removes the csv file that we will not need
os.remove('GT-final_test.csv')
os.chdir('..')

column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
csv_df = pd.DataFrame(csv_list, columns=column_name)
csv_df.to_csv('test_labels.csv', index=None)
print('Successfully created the test_labels csv')


