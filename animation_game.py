# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:13:02 2019

@author: paulh
"""


import numpy as np
import helpers as h
import satellite as s
import celestial as c
import general as g
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

# define space
space1 = g.common_space()


#%% Setting up figure
fig, ax = plt.subplots()
ax.set(xlabel='x (m)', ylabel='y (m)',
       title='Orbit around the Earth')
view_factor = 3
ax.set_xlim([-view_factor*space1.RADIUS_EARTH,view_factor*space1.RADIUS_EARTH])
ax.set_ylim([-view_factor*space1.RADIUS_EARTH,view_factor*space1.RADIUS_EARTH])
ax.set_aspect(aspect=1)

#%% define objects in space
earth = c.celestial(space1, space1.MASS_EARTH)

#%% Plotting the Earth ball
x_earth, y_earth = h.cycle_KO(space1.RADIUS_EARTH,1)
ax.plot(x_earth, y_earth)
ax.grid()
ax.fill_between(x_earth, y_earth, color='#539ecd')

#%% define satellites
                
y_speed_0 = 7800
x_speed_0 = 0
pos_0 = np.array([space1.RADIUS_EARTH*1.1,91000])
satellite1 = s.satellite(space1,1,np.array([x_speed_0,y_speed_0]),pos_0)
space1.satellite_collector.append(satellite1)

y_speed_0 = -8000
x_speed_0 = 0
pos_0 = np.array([space1.RADIUS_EARTH*1.1,-91000])
satellite1 = s.satellite(space1,1,np.array([x_speed_0,y_speed_0]),pos_0)
space1.satellite_collector.append(satellite1)




#for number in range(2):
#    y_speed_0 -= 100
##    x_speed_0 +=50
#    pos_0 = pos_0 + np.array([200000,0])
#    space1.satellite_collector.append(s.satellite(space1,1,np.array([x_speed_0,y_speed_0]),pos_0))
#    
    

#%% Animating Satellite as dot
dt = 50

def orbit_step_n(satellite_n,dt):
    # calculate orbit for next timestep
    satellite_n.new_accel(earth)
    satellite_n.new_pos(dt, earth)
    course_n = satellite_n.pos
    return course_n

x, y = [],[]

for sat in space1.satellite_collector:
    course = orbit_step_n(sat, dt)
    x.append(course[0])
    y.append(course[1])

l, = ax.plot(x, y, '*')   
 

def animate(i):
    # animate next step 
    x, y = [],[]
    
    for sat in space1.satellite_collector:
        course = orbit_step_n(sat, dt)
        x.append(course[0])
        y.append(course[1])
    l.set_xdata(x)
    l.set_ydata(y)
    return l,

ani = animation.FuncAnimation(fig, animate, interval=10)

plt.show()

#ani.save('animation_one_dot.gif',fps=30)

#%% slider for field of view

axcolor = 'lightgoldenrodyellow'
ax_view_factor = plt.axes([0.45, 0.2, 0.5, 0.03], facecolor=axcolor)
delta_view_factor = 0.3
slider_view_factor = Slider(ax_view_factor, 
                            'view factor', 0.5,
                            10, valinit=2, valstep=delta_view_factor)

def update_view_factor(val):
    view_factor = slider_view_factor.val
    ax.set_xlim([-view_factor*space1.RADIUS_EARTH,view_factor*space1.RADIUS_EARTH])
    ax.set_ylim([-view_factor*space1.RADIUS_EARTH,view_factor*space1.RADIUS_EARTH])

slider_view_factor.on_changed(update_view_factor)
