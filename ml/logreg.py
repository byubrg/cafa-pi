import tensorflow as tf
import numpy as np
from .embeddings import load_data_padded, get_batch, shuffle_unison

# Set random seed
np.random.seed(0)

# Import data
data, labels = load_data_padded("./data/example/train_simulated.csv")
data, labels = shuffle_unison(data, labels)
split_point = int(0.9 * len(data))
data_train = data[:split_point]
labels_train = labels[:split_point]
data_test = data[split_point:]
labels_test = labels[split_point:]

# Parameters
learning_rate = 0.01
training_epochs = 1000
batch_size = 100
display_step = 100

# Graph input
x_ = tf.placeholder(tf.float32, [None, 10000]) # seq length (500) x num aminos (20)
x = tf.reshape(x_, [None, 500, 20])
y = tf.placeholder(tf.float32, [None, 3]) # targets: cat, dad, both

# Set model weights
W = tf.Variable(tf.random_normal([10000, 3], stddev=0.1))
b = tf.Variable(tf.zeros([3]))

# Construct model
z = tf.nn.softmax(tf.matmul(x, W2) + b) # Softmax
    
# Define loss and optimizer
#cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
cross_entropy = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

# Initialize the variables (i.e. assign their default value)
#tf.initialize_all_variables().run()
init = tf.global_variables_initializer() 

# Train
with tf.Session() as sess:
   
    # Run initializer
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        # Loop over all batches
        for i in range(1001):
            batch_inputs, batch_targets = get_batch(data_train, labels_train)
            # Run optimization op (backprop) and cost op (to get loss value)
            _, l = sess.run([optimizer, cross_entropy], feed_dict={
                x: batch_inputs,
                y: batch_targets,
            })
        #Display logs per epoch step
        if epoch % display_step == 0:
            print("loss: " + str(l))