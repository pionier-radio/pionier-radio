# -*- coding: utf-8 -*-

import numpy as np
import celestial as c
import general as g
import random

class satellite():
    
    def __init__(self, common_space ,mass, v_inf, pos):
        # initiallize Satellite Properties
        
        self.create_UUID()
        
        self.common_space = common_space
        
        self.mass =  mass # dtype = float
        self.v = v_inf # dtype = np_array
        self.pos = pos # dtype = np_array
        
        self.a = np.zeros((self.common_space.DIMENSIONS,1))
        
        self.bump_radius = 100000 # [m]
        
    def create_UUID(self):
        self.UUID = random.randint(10000,20000)
        print(self.UUID)
        
        
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
        
        # Loop through all satellites in space
        for obj in self.common_space.satellite_collector:
            # make sure to skip itself
            if not(self.UUID==obj.UUID):
                pos_obj = obj.pos
                pos_self = self.pos
                distance = np.linalg.norm(pos_obj-pos_self)
#                print('distance: ',distance)
                if distance < obj.bump_radius + self.bump_radius:
                    self.v, obj.v = self.collision_velocity(self.v, obj.v, self.mass, obj.mass)
            
            
            
    def collision_velocity(self,v1, v2, m1, m2):
        # calculate velocities of two colliding objects after collision
#        print('Velocities before:',v1,v2)
        v1_new =  (m1*v1+m2*(2*v2-v1))/(m1+m2)
        v2_new = (m2*v2+m1*(2*v1-v2))/(m1+m2)
#        print('Velocities after:',v1,v2)    
        return v1_new,v2_new
               
    
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
        
if __name__ == "__main__":
    
    print('\n','_'*80,'\ntesting')
    space = g.common_space()
    v_1 = np.matrix([-3,-4])
    v_2 = np.matrix([10,10])
    pos_1 =  np.matrix([10,10])
    pos_2 = np.matrix([-5,-5])
    test_satellite_1 = satellite(space, 5, v_1, pos_1)
    test_satellite_2 = satellite(space, 3, v_2, pos_2)
    test_earth = c.celestial(space, space.MASS_EARTH)
    
    
    print(test_satellite_1.collision_velocity(v_1,v_2,3,5))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        