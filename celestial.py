# -*- coding: utf-8 -*-

import numpy as np
import general as g

class celestial():
    def __init__(self,common_space, mass):
        
        self.commmon_space = common_space
        
        self.mass = mass
        self.pos = np.zeros((self.commmon_space.DIMENSIONS,1))
    