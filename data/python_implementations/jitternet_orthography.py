# implementation of jitternet orthography using tensorflow

import tensorflow as tf


# Queue for inputs
filename_queue = tf.train.string_input_producer(["jittered_inputs.csv"])




# Setting up how the model will be trained
learning_rate = 0.05
epochs = 10000
batch_size = 100

number_units_input = 286
number_units_hidden_1 = 50
number_units_hidden_2 = 50
number_units_output = 260


# Training data placeholders
input_units = tf.placeholder(tf.float32, [None, number_units_input])
output_units = tf.placeholder(tf.float32, [None, number_units_output])



# Weights and biases
# how do I establish a range? tf.range?:
tf.range(-.18, .18, .01)

weight_matrix_1 = tf.Variable(tf.random_normal([number_units_input, number_units_hidden_1], range = [-.18, .18], mean = 0), name = 'weight_matrix_1')
bias_matrix_1 = tf.Variable(tf.random_normal([number_units_input, number_units_hidden_1]), name = 'bias_matrix_1')

# weights from hidden to output

weight_matrix_3 = tf.Variable(tf.random_normal([number_units_hidden_2, number_units_output],
                                    range = [-.40, .40], mean = 0),
                                    name = 'weight_matrix_3')
