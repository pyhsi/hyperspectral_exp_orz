# -*- coding: utf-8 -*-

import tensorflow as tf
import os
from preprocess import dataset
from c_dcgan import CGAN

flags = tf.app.flags
flags.DEFINE_string("sample_dir", "samples_for_test", "the dir of sample images")
flags.DEFINE_integer("output_size", 176, "the size of generate image")
flags.DEFINE_integer("learn_rate", 0.0002, "the learning rate for gan")
flags.DEFINE_integer("batch_size", 64, "the batch number")
flags.DEFINE_integer("z_dim", 100, "the dimension of noise z")
flags.DEFINE_integer("y_dim", 13, "the dimension of condition y")
flags.DEFINE_string("log_dir", "/tmp/tensorflow_mnist", "the path of tensorflow's log")
flags.DEFINE_string("model_path", "model/model.ckpt", "the path of model")
flags.DEFINE_integer("op", 0, "0: train ; 1:test")

FLAGS = flags.FLAGS

if os.path.exists(FLAGS.sample_dir) == False:
    os.makedirs(FLAGS.sample_dir)
if os.path.exists(FLAGS.log_dir) == False:
    os.makedirs(FLAGS.log_dir)
if os.path.exists(FLAGS.model_path) == False:
    os.makedirs(FLAGS.model_path)

def main(_):
    data_object = dataset('KSC')
    cg = CGAN(data_ob = data_object, sample_dir = FLAGS.sample_dir, output_size=FLAGS.output_size,
              learn_rate=FLAGS.learn_rate, batch_size=FLAGS.batch_size, z_dim=FLAGS.z_dim,
              y_dim=FLAGS.y_dim, log_dir=FLAGS.log_dir, model_path=FLAGS.model_path)
    if FLAGS.op == 0:
        cg.train()
    else:
        cg.test()

if __name__ == '__main__':
    tf.app.run()