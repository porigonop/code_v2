#!/usr/bin/env python2
from openMNIST import load_mnist

images, labels = load_mnist()
dic1 = {}
dic2 = {}
"""
create a dictionnaire with 
the values of the image 
linked to
the number of pixel with the values greater than 200 
divided by the number of images
"""
for image in range(len(labels)):
    for lines in images[image]:
        for pixel in lines:
            if pixel > 125:
                dic1[str(labels[image][0])] = dic1.get(str(labels[image][0]), 0) + 1
	dic2[str(labels[image][0])] = dic2.get(str(labels[image][0]), 0) + 1
print(dic1)
for key in dic1:
    dic1[key] = float(dic1[key]) / dic2[key]
print (dic1)

