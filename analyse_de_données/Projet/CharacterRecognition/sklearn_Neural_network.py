# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
import matplotlib.pyplot as plt
from openMNIST import load_mnist
# Import datasets, classifiers and performance metrics
from sklearn import svm, metrics
import numpy as np
from sklearn.neural_network import MLPClassifier as MLPC

# The data set from MMNIST
images, labels = load_mnist()
images = images[:1000]
labels = labels[:1000]
# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:

n_samples = len(images)

data = images.reshape((n_samples, -1))
print(data[3])

# Create a classifier: a support vector classifier
classifier = MLPC()
labels = np.ravel(labels)
# We learn the digits on the first half of the digits
classifier.fit(data[:n_samples / 2], labels[:n_samples / 2])

# Now predict the value of the digit on the second half:
expected = labels[n_samples / 2:]

predicted = classifier.predict(data[n_samples / 2:])

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

"""
images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))

for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)

plt.show()
"""
