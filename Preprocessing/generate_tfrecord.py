"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=train_labels.csv --image_dir=train --output_path=train.record

  # Create test data:
  python generate_tfrecord.py --csv_input=eval_labels.csv --image_dir=eval --output_path=eval.record
# """
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


def class_text_to_int(row_label):
    if row_label == 'Speed limit (30km/h)':
        return 1
    if row_label == 'Speed limit (50km/h)':
        return 2
    if row_label == 'Speed limit (60km/h)':
        return 3
    if row_label == 'Speed limit (70km/h)':
        return 4
    if row_label == 'Speed limit (80km/h)':
        return 5
    if row_label == 'Speed limit (100km/h)':
        return 6
    if row_label == 'Speed limit (120km/h)':
        return 7
    if row_label == 'No passing':
        return 8
    if row_label == 'No passing for vehicles over 3.5 metric tons':
        return 9
    if row_label == 'Priority road':
        return 10
    if row_label == 'Yield':
        return 11
    if row_label == 'Road work':
        return 12
    if row_label == 'Keep right':
        return 13
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
    print('Successfully created the TFRecord: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
