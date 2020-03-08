import csv

with open('labels.csv', 'r') as currentfile:
    reader = csv.reader(currentfile)
    next(reader)
    with open('label_map.pbtxt', 'w') as label_map:
        for row in reader:

            label_map.write('item {\n')
            # label_map.write('  id: ', int(row[0]) + 1, '\n')
            label_map.write('  id:  ')
            label_map.write(str(int(row[0]) + 1))
            label_map.write('\n')
            # label_map.write('  name: ', "'"+row[1]+"'\n")
            label_map.write('  name:  ')
            label_map.write("'"+row[1]+"'\n")
            label_map.write('}\n')
            label_map.write('\n')


print('Successfully created the label map')
