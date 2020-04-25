import csv
widthList = []
heightList = []


with open('eval_labels.csv', 'r') as currentfile:
    reader = csv.reader(currentfile)
    next(reader)
    for row in reader:
        widthList.append(int(row[1]))
        heightList.append(int(row[2]))


print("Average Width:", sum(widthList)/len(widthList))
print("Average Height:", sum(heightList)/len(heightList))
