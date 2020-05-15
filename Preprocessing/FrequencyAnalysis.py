import csv
import pandas as pd
classFrequencyTrain = {}
classFrequencyEval = {}
csv_list = []

# Reading csv file and iteratively storing class instances
with open('train_labels.csv', 'r') as currentfile:
    reader = csv.reader(currentfile)
    next(reader)
    for row in reader:
        if row[3] not in classFrequencyTrain:
            classFrequencyTrain[row[3]] = 1
        else:
            classFrequencyTrain[row[3]] += 1

# Reading csv file and iteratively storing class instances
with open('eval_labels.csv', 'r') as currentfile:
    reader = csv.reader(currentfile)
    next(reader)
    for row in reader:
        if row[3] not in classFrequencyEval:
            classFrequencyEval[row[3]] = 1
        else:
            classFrequencyEval[row[3]] += 1


# Combining the 2 dictionaries used with the same key holding a tupple with both number of Images in the Train Set
# and the number of images in the Evaluation set as its key
classFrequencies = dict([(k, [classFrequencyTrain[k], classFrequencyEval[k]]) for k in classFrequencyTrain])

# Sorting the dictionary by number of images
for i in sorted(classFrequencies.items(), key=lambda x: x[1], reverse=True):
    value = i[0], i[1][0], i[1][1]
    csv_list.append(value)

# Creating a csv file storing the results which can be then visualized 
column_name = ['class', 'numTrainImages', 'numEvalImages']
csv_df = pd.DataFrame(csv_list, columns=column_name)
csv_df.to_csv('FrequencyAnalysis.csv', index=None)

