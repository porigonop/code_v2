# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt
from openMNIST import load_mnist
import numpy as np
# Import datasets, classifiers and performance metrics
from sklearn import svm, metrics
from sklearn.cross_validation import train_test_split

n_samples = 1000
# The data set from MMNIST
images, labels = load_mnist()
images = images[:n_samples]
labels = labels[:n_samples]
# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
images = images.reshape((n_samples, -1))
images_train, images_test, labels_train, labels_test = train_test_split(images, labels)
print(images_train.shape, labels_train.shape)
print(images_train[1])
"""
images_train = images_train.reshape((n_samples, -1))
images_test = images_test.reshape((n_samples, -1))
"""

# data = images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
classifier = svm.SVC()

# We learn the digits on the first half of the digits
classifier.fit(images_train, labels_train)

# Now predict the value of the digit on the second half:
expected = labels_test

predicted = classifier.predict(images_test)
print(predicted[1])
print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

