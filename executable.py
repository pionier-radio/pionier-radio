# -*- coding: utf-8 -*-
import numpy as np
import satellite as s
import celestial as c
import general as g
import matplotlib.pyplot as plt



space1 = g.common_space()



print(space1.GAMMA)

earth = c.celestial(space1, space1.MASS_EARTH)
satellite1 = s.satellite(space1,3,np.array([0,80]),np.array([space1.RADIUS_EARTH,0]))

satellite1.mass

dt = 1
n = 10
pos_verlauf=np.zeros((n,space1.DIMENSIONS))

for t in range(n):
    
    satellite1.new_accel(earth)
    satellite1.new_pos(dt)

    pos_verlauf[t,:]=satellite1.pos


plt.scatter(pos_verlauf[:,0],pos_verlauf[:,1])