# -*- coding: utf-8 -*-

import numpy as np
import general as g


class celestial():
    def __init__(self,common_space, mass):
        
        self.commmon_space = common_space
        
        self.radius = 0
        self.mass = mass # kg
        self.pos = np.zeros((self.commmon_space.DIMENSIONS,1)) # [m.m]
        
        self.atmos_calc_limit = self.radius + 500000 # [m] up to this atmospheric influences will be considered
        
        self.atmosphere_pressure_surface = 10**5  # Pa 
        self.ideal_gas_constant = 287 # J/(kg mol)
        
        
    def pressure_at_h1(self,h1):
        
        R = self.ideal_gas_constant
        T = 300 # temperature at heigt h1
        M = self.mass
        g_a = self.commmon_space.GAMMA*self.mass/(h1) # Gravitational accel aat height h1
        
        p_h1= np.exp(-(g_a*M*(h1-self.radius))/(R*T))
        
        return p_h1
    

if __name__ == "__main__":
    
    print('\n','_'*80,'\ntesting')
    test_space = g.common_space()
    test_earth = celestial(test_space, test_space.MASS_EARTH)
    
    