import pickle
import numpy as np
import random
import tensorflow as tf

with open('F:/MojSUNS/train.pickle', 'rb') as f:
    save = pickle.load(f)
    datasetTrain = save['datasetTrain']
    labelsTrain = save['labelsTrain']
with open('F:/MojSUNS/valid.pickle', 'rb') as f:
    saveValid = pickle.load(f)
    datasetValid = saveValid['datasetValid']
    labelsValid = saveValid['labelsValid']
with open('F:/MojSUNS/test2.pickle', 'rb') as g:
    saveTest = pickle.load(g)
    datasetTest = saveTest['datasetTest']
    labelsTest = saveTest['labelsTest']


def reformat(dataset, labels):
  #dataset = dataset.reshape((-1, 100 * 100)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  list = []
  labelsList = []
  for i in range(0, 48):
      for j in range(0, int(len(dataset[i])/10)):
          list.append(dataset[i][j - 1].reshape(1, 100 * 100 * 3))
          #list.append(dataset[i][random.randint(0, dataset[i].shape[0]) - 1].reshape(1, 100 * 100 * 3))
          labelsList.append(labels[i])
  newdb1 = list[0]
  labels1 = []
  labels1.append((np.arange(48) == labelsList[0]-1).astype(np.float32))
  for i in range(1, len(list)):
      newdb1 = np.concatenate((newdb1, list[i]), axis=0)
      labels1.append((np.arange(48) == labelsList[i]-1).astype(np.float32))
  return newdb1, labels1#labelsList

def reformatEh(dataset, labels):
  labelsN = []
  for i in labels:
      labelsN.append(i-1)
  labels = labelsN
  #dataset = dataset.reshape((-1, 100 * 100)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  list = []
  labelsList = []
  for i in range(0, 48):
      for j in range(0, 20):    #int(len(dataset[i])/10)
          list.append(dataset[i][j - 1].reshape(-1, 100 * 100 * 3))
          #list.append(dataset[i][random.randint(0, dataset[i].shape[0]) - 1].reshape(1, 100 * 100 * 3))
          labelsList.append(labels[i])
  newdb1 = list[0]
  labels1 = []
  labels1.append((np.arange(48) == labelsList[0]).astype(np.float32))
  for i in range(1, len(list)):
      newdb1 = np.concatenate((newdb1, list[i]), axis=0)
      labels1.append((np.arange(48) == labelsList[i]).astype(np.float32))

  return newdb1, labels1#labelsList

def reformatEh1(dataset, labels):
  labelsN = []
  for i in labels:
      labelsN.append(i-1)
  labels = labelsN
  #dataset = dataset.reshape((-1, 100 * 100)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  list = []
  labelsList = []
  for i in range(0, 48):
      for j in range(0, 5):    #int(len(dataset[i])/10)
          list.append(dataset[i][j - 1].reshape(-1, 100 * 100 * 3))
          #list.append(dataset[i][random.randint(0, dataset[i].shape[0]) - 1].reshape(1, 100 * 100 * 3))
          labelsList.append(labels[i])
  newdb1 = list[0]
  labels1 = []
  labels1.append((np.arange(48) == labelsList[0]).astype(np.float32))
  for i in range(1, len(list)):
      newdb1 = np.concatenate((newdb1, list[i]), axis=0)
      labels1.append((np.arange(48) == labelsList[i]).astype(np.float32))
  return newdb1, labels1#labelsList

def reformatEh2(dataset, labels):
  labelsN = []
  for i in labels:
      labelsN.append(i-1)
  labels = labelsN
  #dataset = dataset.reshape((-1, 100 * 100)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  list = []
  labelsList = []
  for i in range(0, 48):
      for j in range(0, 5):    #int(len(dataset[i])/10)
          list.append(dataset[i][j - 1].reshape(-1, 100 * 100 * 3))
          #list.append(dataset[i][random.randint(0, dataset[i].shape[0]) - 1].reshape(1, 100 * 100 * 3))
          labelsList.append(labels[i])
  newdb1 = list[0]
  labels1 = []
  labels1.append((np.arange(48) == labelsList[0]).astype(np.float32))
  for i in range(1, len(list)):
      newdb1 = np.concatenate((newdb1, list[i]), axis=0)
      labels1.append((np.arange(48) == labelsList[i]).astype(np.float32))
  return newdb1, labels1#labelsList

def reformat1(dataset, labels):
  #dataset = dataset.reshape((-1, 100 * 100)).astype(np.float32)
  # Map 0 to [1.0, 0.0, 0.0 ...], 1 to [0.0, 1.0, 0.0 ...]
  list = []
  labelsList = []
  for i in range(0, 48):
      for j in range(0, int(len(dataset[i])/10)):
          list.append(dataset[i][j - 1].reshape(1, 100 * 100 * 3))
          #list.append(dataset[i][random.randint(0, dataset[i].shape[0]) - 1].reshape(1, 100 * 100 * 3))
          labelsList.append(labels[i])
  newdb1 = list[0]
  labels1 = []
  labels1.append((np.arange(48) == labelsList[0]-2).astype(np.float32))
  for i in range(1, len(list)):
      newdb1 = np.concatenate((newdb1, list[i]), axis=0)
      labels1.append((np.arange(48) == labelsList[i]-2).astype(np.float32))
  return newdb1, labels1#labelsList


valid_dataset, valid_labels = reformatEh1(datasetValid, labelsValid)
train_dataset, train_labels = reformatEh(datasetTrain, labelsTrain)
test_dataset, test_labels = reformatEh2(datasetTest, labelsTest)
print('Training set', len(train_dataset), len(train_labels))
print('Validation set', len(valid_dataset), len(valid_labels))
print('Test set', len(test_dataset), len(test_labels))


# import matplotlib.pyplot as plt
# plt.imshow(valid_dataset[5].reshape(100,100,3))
# print(valid_labels[5])
# plt.show()
# plt.imshow(valid_dataset[300].reshape(100,100,3))
# print(valid_labels[300])
# plt.show()
# plt.imshow(valid_dataset[540].reshape(100,100,3)+0.5)
# print(valid_labels[540])
# plt.show()
# plt.imshow(train_dataset[12].reshape(100,100,3))
# print(train_labels[12])
# plt.show()
# plt.imshow(train_dataset[1548].reshape(100,100,3))
# print(train_labels[1548])
# plt.show()
# plt.imshow(train_dataset[2850].reshape(100,100,3) + 0.5)
# print(train_labels[2850])
# plt.show()

def accuracy(predictions, labels):
  return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1)) / predictions.shape[0])     # 010 ... argmax: 1 .... 010... argmax 1... 1 == 1

print("___________________________________")

def uloha1():
  num_nodes= 1024
  batch_size = 128
  beta = 0.01

  graph = tf.Graph()
  with graph.as_default():

      # Input data. For the training data, we use a placeholder that will be fed
      # at run time with a training minibatch.
      tf_train_dataset = tf.placeholder(tf.float32, shape=(batch_size, 100 * 100 * 3))
      tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size, 48))
      tf_valid_dataset = tf.constant(valid_dataset)
      tf_test_dataset = tf.constant(test_dataset)

      # Variables.
      weights_1 = tf.Variable(tf.truncated_normal([100 * 100 * 3, num_nodes]))
      biases_1 = tf.Variable(tf.zeros([num_nodes]))
      weights_2 = tf.Variable(tf.truncated_normal([num_nodes, 48]))
      biases_2 = tf.Variable(tf.zeros([48]))

      # Training computation.
      logits_1 = tf.matmul(tf_train_dataset, weights_1) + biases_1
      relu_layer= tf.nn.relu(logits_1)
      logits_2 = tf.matmul(relu_layer, weights_2) + biases_2
      # Normal loss function
      loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits_2, labels=tf_train_labels))

      # Optimizer.
      optimizer = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

      # Predictions for the training
      train_prediction = tf.nn.softmax(logits_2)

      # Predictions for validation
      logits_1 = tf.matmul(tf_valid_dataset, weights_1) + biases_1
      relu_layer= tf.nn.relu(logits_1)
      logits_2 = tf.matmul(relu_layer, weights_2) + biases_2

      valid_prediction = tf.nn.softmax(logits_2)

      # Predictions for test
      logits_1 = tf.matmul(tf_test_dataset, weights_1) + biases_1
      relu_layer= tf.nn.relu(logits_1)
      logits_2 = tf.matmul(relu_layer, weights_2) + biases_2

      test_prediction =  tf.nn.softmax(logits_2)
  import math
  num_steps = 801
  xBatch = []
  yBatch = []
  xValid = []
  yValid = []

  train_label = np.asarray(train_labels)


  with tf.Session(graph=graph) as session:
      tf.initialize_all_variables().run()
      print("Initialized")
      for step in range(num_steps):
          # Pick an offset within the training data, which has been randomized.
          # Note: we could use better randomization across epochs.

          offset = (step * batch_size) % ((train_label.shape[0]) - batch_size)
          # Generate a minibatch.
          batch_data = train_dataset[offset:(offset + batch_size), :]
          batch_labels = train_label[offset:(offset + batch_size), :]
          # Prepare a dictionary telling the session where to feed the minibatch.
          # The key of the dictionary is the placeholder node of the graph to be fed,
          # and the value is the numpy array to feed to it.
          feed_dict = {tf_train_dataset : batch_data, tf_train_labels : batch_labels}   #[1,3,5,9,45,41,45,48,48,48,....128]    128riadkov 1 stlpec....
                                                                                        #1 .... 1 0 0 0 0 0 0 0 0 0 0 _48stlpcov
                                                                                        #3..... 0 0 1 0 0 00 0 0 0 ....
          _, l, predictions = session.run([optimizer, loss, train_prediction], feed_dict=feed_dict)
          if (step % 100 == 0):
              print("Minibatch loss at step {}: {}".format(step, l))
              print("Minibatch accuracy: {:.1f}".format(accuracy(predictions, batch_labels)))
              yBatch.append(math.floor(accuracy(predictions, batch_labels)*10)/10)
              print("Validation accuracy: {:.1f}".format(accuracy(valid_prediction.eval(), valid_labels)))
              yValid.append(math.floor(accuracy(valid_prediction.eval(), valid_labels)*10)/10)
      print("Test accuracy: {:.1f}".format(accuracy(test_prediction.eval(), test_labels)))
      import pylab as pl
      xValid = [0,100,200,300,400,500,600,700,800]
      xBatch = [0,100,200,300,400,500,600,700,800]
      #xValid = [0,500,1000,1500,2000,2500,3000]
      #xBatch = [0,500,1000,1500,2000,2500,3000]
      pl.plot(xValid, yValid,'go-', label="Validation")
      pl.plot(xBatch, yBatch,'bo-', label="Minibatch")
      pl.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
      pl.suptitle("Test Accuracy: " + str(math.floor(accuracy(test_prediction.eval(), test_labels)*10)/10) + "%")
      pl.show()

uloha1()
