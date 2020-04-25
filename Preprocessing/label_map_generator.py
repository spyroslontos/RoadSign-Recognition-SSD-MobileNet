import csv

with open('labels.csv', 'r') as currentfile:
    reader = csv.reader(currentfile)
    next(reader)
    with open('label_map.pbtxt', 'w') as label_map:
        for i, row in enumerate(reader, start=1):

            label_map.write('item {\n')
            label_map.write('  id:  ')
            label_map.write(str(i))
            label_map.write('\n')
            label_map.write('  name:  ')
            label_map.write("'"+row[1]+"'\n")
            label_map.write('}\n')
            label_map.write('\n')


print('Successfully created the label map')
