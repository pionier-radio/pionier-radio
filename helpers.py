# -*- coding: utf-8 -*-

import numpy as np

def cycle_KO(radius, discretisation, x=0, y=0):
    # Returns cartesian coordinates x and y for a cycle of given radius 
    # E.g.: discretisation = 1 --> one point per degree
    
    t = np.linspace(0,2*np.pi,360*discretisation)
    
    x = np.cos(t)*radius + x
    y = np.sin(t)*radius + y
    
    return x,y 

