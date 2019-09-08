# -*- coding: utf-8 -*-

import numpy as np
import celestial as c
import general as g

class satellite():
    
    def __init__(self, common_space ,mass, v_inf, pos):
        # initiallize Satellite Properties
        
        self.common_space = common_space
        
        self.mass =  mass # dtype = float
        self.v = v_inf # dtype = np_array
        self.pos = pos # dtype = np_array
        
        self.a = np.zeros((self.common_space.DIMENSIONS,1))
        
        self.bump_radius = 90000 # [m]
        
        
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
        
        self.collision_check()
        
    def collision_check(self):
        # parses an Object_collector (with all other satellites) 
        # checks if distances lie out of both bump_radii 
        # if they collide, calculate velocities after collision
        
        for obj in self.common_space.satellite_collector:
            pos_obj = obj.pos
            pos_self = self.pos
            distance = np.linalg.norm(pos_obj-pos_self)
            if distance < obj.bump_radius + self.bump_radius:
                v_self, v_obj = self.collision_velocity(self.v, obj.v, self.mass, obj.mass)
                
    def collision_velocity(self,v1, v2, m1, m2):
        # calculate velocities of two colliding objects after collision
        print('Velocities before:',v1,v2)
        
        v1 = (m1*v1+m2*(2*v2-v1))/(m1+m2)
        v2 = (m1*v1+m2*(2*v2-v1))/(m1+m2)
        print('Velocities after:',v1,v2)
        
        return v1,v2
               
    
    def atmospherical_properties(self, Cd):
        # Cd: Drag coefficient [-] (dtype=float)
        # get aerodynamic properties of S/C and return v-reduction factor
        
        factor = (1-Cd)
        # WRONG FORMULA --- TO BE CORRECTED IN THE FUTURE
        return factor
    
    
    def new_accel(self, celestial):
        # calculate new acceleration 'self.a' with curren position 'self.pos'
        gamma = self.common_space.GAMMA
        
        r = self.pos - np.transpose(celestial.pos)
        r_abs = np.linalg.norm(r)
        
        self.a = -self.pos * gamma * (celestial.mass)/r_abs**3
        
#        print('accel: ',np.round(self.a))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        