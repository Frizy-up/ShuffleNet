import tensorflow as tf
import numpy as np


############### test channel shuffle  ###########################################
# def channel_shuffle(name, x, num_groups):
#     with tf.variable_scope(name) as scope:
#         n, h, w, c = x.shape.as_list()
#         x_reshaped = tf.reshape(x, [-1, h, w, num_groups, c // num_groups])
#         print(np.shape(x_reshaped),x_reshaped.eval())
#
#         x_transposed = tf.transpose(x_reshaped, [0, 1, 2, 4, 3])
#         print(np.shape(x_transposed), x_transposed.eval())
#
#         output = tf.reshape(x_transposed, [-1, h, w, c])
#         return output
#
#
#
# c = tf.ones([1,2,2,4])
# sess = tf.InteractiveSession().as_default()
# print c.eval()
#
# c0 = c[:,:,:,0]*1
# c1 = c[:,:,:,1]*2
# c2 = c[:,:,:,1]*3
# c3 = c[:,:,:,1]*4
#
# c0 = tf.expand_dims(c0,-1)
# c1 = tf.expand_dims(c1,-1)
# c2 = tf.expand_dims(c2,-1)
# c3 = tf.expand_dims(c3,-1)
#
#
# x = tf.concat([c0,c1,c2,c3],3)
#
# print(x.eval())
#
# out = channel_shuffle("test_shuffle",x,2)
# print out.eval()
###################################################################################



############################### test load json ####################################
import json

config = './config/test.json'

with open(config, 'r') as config_file:
    config_args_dict = json.load(config_file)
    print(config_args_dict)

###################################################################################





