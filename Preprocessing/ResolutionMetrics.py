import csv
widthList = []
heightList = []

files = ['train_labels.csv', 'eval_labels.csv', 'test_labels.csv']

for file in files:
    with open(file, 'r') as currentfile:
        reader = csv.reader(currentfile)
        next(reader)
        for row in reader:
            widthList.append(int(row[1]))
            heightList.append(int(row[2]))


print("Min Width:", min(widthList))
print("Min Height:", min(heightList))
print('--------------------')
print("Max Width:", max(widthList))
print("Max Height:", max(heightList))
print('--------------------')
print("Average Width:", sum(widthList)/len(widthList))
print("Average Height:", sum(heightList)/len(heightList))
