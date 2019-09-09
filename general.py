# -*- coding: utf-8 -*-

import numpy as np


# define general properties of physical space 
class common_space():
    
    def __init__(self):
        self.GAMMA = 6.67408 * 10**(-11)
        self.DIMENSIONS = 2
        
        self.MASS_EARTH = 5.972*10**24
        self.RADIUS_EARTH = 6.731 * 10**6
        
        self.satellite_collector = []
    def orbit(self, dt, n, sat, celestial):
        # calculate orbit over n timesteps of size dt
        course = np.zeros((n,self.DIMENSIONS))
        for t in range(n):
            sat.new_accel(celestial)
            sat.new_pos(dt, celestial)
            course[t,:]=sat.pos
            
        return course
