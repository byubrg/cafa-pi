import tensorflow as tf
import numpy as np
from .embeddings import load_data_padded, get_batch, shuffle_unison, H5pyDao
import random

tf.logging.set_verbosity(tf.logging.WARN)

SEQ_LEN = 500
NUM_CHARS = 20
NUM_TARGETS = 3

if __name__ == "__main__":
    random.seed(0)
    inputs = tf.placeholder(tf.float32, [None, SEQ_LEN, NUM_CHARS], "sequence")
    targets = tf.placeholder(tf.float32, [None, NUM_TARGETS])
    conv1 = tf.layers.conv1d(inputs=inputs, filters=32, kernel_size=(5,), padding="same", activation=tf.nn.relu)
    conv2 = tf.layers.conv1d(inputs=conv1, filters=64, kernel_size=(5,), padding="same", activation=tf.nn.relu)
    conv3 = tf.layers.conv1d(inputs=conv2, filters=128, kernel_size=(5,), padding="same", activation=tf.nn.relu)
    flattened = tf.contrib.layers.flatten(conv3)
    fc1 = tf.contrib.layers.fully_connected(flattened, 128)
    outputs = tf.contrib.layers.fully_connected(fc1, NUM_TARGETS, activation_fn=tf.nn.sigmoid)
    loss = tf.losses.mean_squared_error(targets, outputs)
    tf.summary.scalar("mse", loss)
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        train_writer = tf.summary.FileWriter("log/train", sess.graph)
        test_writer = tf.summary.FileWriter("log/test", sess.graph)
        tf.global_variables_initializer().run()
        # data, labels = load_data_padded("./data/example/train_simulated.csv")
        
        # data, labels = shuffle_unison(data, labels)
        # split_point = int(0.9 * len(data))
        # data_train = data[:split_point]
        # labels_train = labels[:split_point]
        # data_test = data[split_point:]
        # labels_test = labels[split_point:]
        dao = H5pyDao("./data/example/train_simulated.h5", percent_test=10,
                      csv_path="./data/example/train_simulated.csv")
        
        for i in range(1001):
            # batch_inputs, batch_targets = get_batch(data_train, labels_train)
            batch_inputs, batch_targets = dao.get_batch_train()
            summary, train_loss, _ = sess.run([merged, loss, optimizer], feed_dict={
                inputs: batch_inputs,
                targets: batch_targets,
            })
            train_writer.add_summary(summary, i)
            if i % 100 == 0:
                # batch_inputs, batch_targets = get_batch(data_test, labels_test)
                batch_inputs, batch_targets = dao.get_batch_test()
                summary, test_loss = sess.run([merged, loss], feed_dict={
                    inputs: batch_inputs,
                    targets: batch_targets
                })
                test_writer.add_summary(summary, i)
                print("Iteration {i}, test loss {mse}".format(i=i, mse=test_loss))
    dao.cleanup()