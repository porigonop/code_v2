#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import math




def distance(p1, p2):
    l = QLineF(p1, p2)
    return l.length()

def angle(p1, p2, p3):
    l1 = QLineF(p1, p2)
    l2 = QLineF(p1, p3)
    
    angle = l2.angleTo(l1)
    if angle > 180:
        angle = 360 - angle
    return angle
    
def deg_to_rad(angle):
    return angle * math.pi / 180.0
    
def longueur_cote_oppose(angle, longueur_hypotenuse):
    #print('angle: ', angle)
    #print('longueur_hypotenuse: ', longueur_hypotenuse)
    return math.sin(deg_to_rad(angle)) * longueur_hypotenuse

def concate_poly(poly1, poly2):
    result = QPolygon()
    for elt in poly1:
        result.append(elt)

    for elt in poly2:
        result.append(elt)
    return result

def DouglasPeucker(polygon, epsilon):
    # Trouve le point le plus eloigne du segment.
    dmax = 0
    dmin = 0
    elt_end = polygon.at(polygon.size() - 1)
    for i in range (1, polygon.size() - 1):
        d = longueur_cote_oppose(angle(polygon.at(0),\
                                       elt_end,\
                                       polygon.at(i)),\
                                 distance(polygon.at(0),\
                                          polygon.at(i)))
        if d > dmax:
          index = i
          dmax = d

    
    # Si la distance dmax est supérieure au seuil, on simplifie.
    if dmax >= epsilon:
        poly1 = QPolygon()
        poly2 = QPolygon()

        for i in range(index+1) : 
            poly1.append(polygon.at(i))

        for i in range(index, polygon.size()):
            poly2.append(polygon.at(i))
	
        recResult1 = DouglasPeucker(poly1, epsilon)
        recResult2 = DouglasPeucker(poly2, epsilon)
        
        result = concate_poly(recResult1, recResult2)
        
    # Tous les points sont proches. -> renvoie un segment avec les extrémités.
    else:
        result = QPolygon()
        result.append(polygon.at(0))
        result.append(elt_end)
        
    return result


