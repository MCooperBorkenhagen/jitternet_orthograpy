# implementation of jitternet orthography using tensorflow

import tensorflow as tf


# Queue for inputs
filename_queue = tf.train.string_input_producer(["jittered_inputs.csv"])




# Setting up how the model will be trained
graphicSize = 28
numOutputs = 10
learning_rate = 0.5
epochs = 10
batch_size = 100

numUnits_hidden1 = 300
