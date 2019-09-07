# -*- coding: utf-8 -*-
import numpy as np
import helpers as h
import satellite as s
import celestial as c
import general as g
import matplotlib.pyplot as plt
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
y_speed_0 = 8000
x_speed_0 = 0
pos_0 = np.array([space1.RADIUS_EARTH*1.1,0])
satellite1 = s.satellite(space1,1,np.array([x_speed_0,y_speed_0]),pos_0)

#%% Plotting the Earth ball
x_earth, y_earth = h.cycle_KO(space1.RADIUS_EARTH,1)
ax.plot(x_earth, y_earth)
ax.grid()
ax.fill_between(x_earth, y_earth, color='#539ecd')
                
                
def orbit(dt, n):
    # calculate orbit over timesteps

    course=np.zeros((n,space1.DIMENSIONS))
    for t in range(n):
        satellite1.new_accel(earth)
        satellite1.new_pos(dt)
        course[t,:]=satellite1.pos
        
    return course

dt = 10
n = 10000
course = orbit(dt,n)

#%% plot satellites orbit
l, = ax.plot(course[:,0],course[:,1],linewidth=0.3)


#%% Define slider for view factor
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

#%% Define slider for initial speed y
axcolor = 'lightgoldenrodyellow'
ax_init_speed_y = plt.axes([0.45, 0.8, 0.5, 0.03], facecolor=axcolor)
delta_speed = 100
slider_y_speed = Slider(ax_init_speed_y, 
                        'initial speed (m/s)', y_speed_0*0.5, y_speed_0*1.5, 
                        valinit=y_speed_0, valstep=delta_speed)

def update_init_speed_y(val):
    y_speed = slider_y_speed.val
    
    # define starting position
    satellite1.v = np.array([x_speed_0,y_speed])
    satellite1.pos = pos_0
    
    # get new position 
    course = orbit(dt,n)
    # update figure
    l.set_xdata(course[:,0])
    l.set_ydata(course[:,1])
    fig.canvas.draw_idle()
    
slider_y_speed.on_changed(update_init_speed_y)

#%% Define slider for initial speed x

axcolor = 'lightgoldenrodyellow'
ax_init_speed_x = plt.axes([0.45, 0.75, 0.5, 0.03], facecolor=axcolor)
delta_speed = 100
slider_x_speed = Slider(ax_init_speed_x, 
                        'initial speed (m/s)', y_speed_0*0.5, y_speed_0*1.5, 
                        valinit=y_speed_0, valstep=delta_speed)

def update_init_speed_x(val):
    y_speed = slider_y_speed.val
    x_speed = slider_x_speed.val
    # define starting position
    satellite1.v = np.array([x_speed,y_speed])
    satellite1.pos = pos_0
    
    # get new position 
    course = orbit(dt,n)
    # update figure
    l.set_xdata(course[:,0])
    l.set_ydata(course[:,1])
    fig.canvas.draw_idle()    
    
    
    


plt.show()










