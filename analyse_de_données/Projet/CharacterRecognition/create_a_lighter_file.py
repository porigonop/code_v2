#!/usr/bin/env python3
import scipy.misc
from openMNIST import load_mnist
"""
allow the user to create in a file "images" the 100 first image in the 
dataset 
"""
images, labels = load_mnist()
for x in range(100):
    scipy.misc.imsave("./images/" + str(labels[x]) + str(x) + ".jpeg", images[x])

