# -*- coding: utf-8 -*-

import numpy as np

def cycle_KO(radius, discretisation, x=0, y=0):
    # Returns cartesian coordinates x and y for a cycle of given radius 
    # E.g.: discretisation = 1 --> one point per degree
    
    t = np.linspace(0,2*np.pi,360*discretisation)
    
    x = np.cos(t)*radius + x
    y = np.sin(t)*radius + y
    
    return x,y 

def perpendicular_norm_vector(vector):
    
    # Returns 2d normed vector, perpendicular to input vector
    vector_per = np.zeros([2,1])
    vector_per[0]=1
    vector_per[1] = -(vector[0]/vector[1])
    
    # norm vector to length=1
    abs_vector_per = np.linalg.norm(vector_per)
    vector_per_norm = vector_per/abs_vector_per
    
    return vector_per_norm

def angle_vector(a,b):
    # returns angle between two vectors a and b
    c = np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b) # -> cosine of the angle
    angle = np.arccos(np.clip(c, -1, 1)) # if you really want the angle
    return angle

def check_direction(a,b):
    # returns -1 if a and b point in opposite directions and
    # returns 1 if a and b point in the same direction
    
    temp = angle_vector(a,b)
    if (temp > np.pi/2): return 1
    elif (temp < np.pi/2): return -1
    else: return 0
    