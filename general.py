# -*- coding: utf-8 -*-

import numpy as np


# define general properties of physical space 
class common_space():
    
    def __init__(self):
        self.GAMMA = 6.67408 * 10**(-11)
        self.DIMENSIONS = 2
        
        self.MASS_EARTH = 5.972*10**24
        self.RADIUS_EARTH = 6.731 * 10**6