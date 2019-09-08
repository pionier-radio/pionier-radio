# -*- coding: utf-8 -*-

import numpy as np
import celestial as c
import general as g

class satellite():
    
    def __init__(self, common_space ,mass, v_inf, pos):
        # initiallize Satellite Properties
        
        self.commmon_space = common_space
        
        self.mass =  mass # dtype = float
        self.v = v_inf # dtype = np_array
        self.pos = pos # dtype = np_array
        
        self.a = np.zeros((self.commmon_space.DIMENSIONS,1))
        
    def new_pos(self, dt, celestial):
        # calculate new position 'self.pos' with current speed 'self.v'
        # after a time increment 'dt' (dtype=float)
        self.new_speed(dt, celestial)
        self.pos = self.pos + dt * self.v
        
    def new_speed(self, dt, celestial):
        # calculate new speed 'self.v' with curren position 'self.pos'
        # after a time increment 'dt' (dtype=float)
        self.v = self.v +  dt * self.a
        r = self.pos - np.transpose(celestial.pos)
        r_abs = np.linalg.norm(r)
        
        Cd = 0.06 
        atmos_factor = self.atmospherical_properties(Cd)
        
        if r_abs < celestial.atmos_calc_limit:
            self.v = atmos_factor * self.v 
        
    
    def atmospherical_properties(self, Cd):
        # Cd: Drag coefficient [-] (dtype=float)
        # get aerodynamic properties of S/C and return v-reduction factor
        
        factor = (1-Cd)
    
        return factor
    
    
    def new_accel(self, celestial):
        # calculate new acceleration 'self.a' with curren position 'self.pos'
        gamma = self.commmon_space.GAMMA
        
        r = self.pos - np.transpose(celestial.pos)
        r_abs = np.linalg.norm(r)
        
        self.a = -self.pos * gamma * (celestial.mass)/r_abs**3
        
#        print('accel: ',np.round(self.a))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        