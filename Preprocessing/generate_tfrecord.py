"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=train_labels.csv --image_dir=train --output_path=train.record

  # Create test data:
  python generate_tfrecord.py --csv_input=test_labels.csv --image_dir=test --output_path=test.record
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
flags.DEFINE_string('image_dir', '', 'Path to images')
FLAGS = flags.FLAGS


# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'Speed limit (20km/h)':
        return 1
    if row_label == 'Speed limit (30km/h)':
        return 2
    if row_label == 'Speed limit (50km/h)':
        return 3
    if row_label == 'Speed limit (60km/h)':
        return 4
    if row_label == 'Speed limit (70km/h)':
        return 5
    if row_label == 'Speed limit (80km/h)':
        return 6
    if row_label == 'End of speed limit (80km/h)':
        return 7
    if row_label == 'Speed limit (100km/h)':
        return 8
    if row_label == 'Speed limit (120km/h)':
        return 9
    if row_label == 'No passing':
        return 10
    if row_label == 'No passing for vehicles over 3.5 metric tons':
        return 11
    if row_label == 'Right-of-way at the next intersection':
        return 12
    if row_label == 'Priority road':
        return 13
    if row_label == 'Yield':
        return 14
    if row_label == 'Stop':
        return 15
    if row_label == 'No vehicles':
        return 16
    if row_label == 'Vehicles over 3.5 metric tons prohibited':
        return 17
    if row_label == 'No entry':
        return 18
    if row_label == 'General caution':
        return 19
    if row_label == 'Dangerous curve to the left':
        return 20
    if row_label == 'Dangerous curve to the right':
        return 21
    if row_label == 'Double curve':
        return 22
    if row_label == 'Bumpy road':
        return 23
    if row_label == 'Slippery road':
        return 24
    if row_label == 'Road narrows on the right':
        return 25
    if row_label == 'Road work':
        return 26
    if row_label == 'Traffic signals':
        return 27
    if row_label == 'Pedestrians':
        return 28
    if row_label == 'Children crossing':
        return 29
    if row_label == 'Bicycles crossing':
        return 30
    if row_label == 'Beware of ice/snow':
        return 31
    if row_label == 'Wild animals crossing':
        return 32
    if row_label == 'End of all speed and passing limits':
        return 33
    if row_label == 'Turn right ahead':
        return 34
    if row_label == 'Turn left ahead':
        return 35
    if row_label == 'Ahead only':
        return 36
    if row_label == 'Go straight or right':
        return 37
    if row_label == 'Go straight or left':
        return 38
    if row_label == 'Keep right':
        return 39
    if row_label == 'Keep left':
        return 40
    if row_label == 'Roundabout mandatory':
        return 41
    if row_label == 'End of no passing':
        return 42
    if row_label == 'End of no passing by vehicles over 3.5 metric tons':
        return 43
    else:
        return 0


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_png = fid.read()
    encoded_png_io = io.BytesIO(encoded_png)
    image = Image.open(encoded_png_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'png'
    ymins = []
    xmins = []
    ymaxs = []
    xmaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        ymins.append(row['ymin'] / height)
        xmins.append(row['xmin'] / width)
        ymaxs.append(row['ymax'] / height)
        xmaxs.append(row['xmax'] / width)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/width': dataset_util.int64_feature(width),
        'image/height': dataset_util.int64_feature(height),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_png),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    path = os.path.join(FLAGS.image_dir)
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
