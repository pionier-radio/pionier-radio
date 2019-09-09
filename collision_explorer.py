


import numpy as np
import helpers as h
import satellite as s
import celestial as c
import general as g
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from random import randint

class Ball():
    
    def __init__(self, MASS, VEL, POS):
        
        self.create_UUID()
        
        self.mass = MASS
        self.vel = VEL
        self.pos = POS
        
        self.size = 1 
        
        self.state='free'
        
    def create_UUID(self):
        self.UUID = randint(10000,20000)
        print(self.UUID)
        
    
    def collision_check(self, collec):
        # parses an Object_collector (with all other satellites) 
        # checks if distances lie out of both bump_radii 
        # if they collide, calculate velocities after collision
        
        # Loop through all satellites in space
        for obj in collec:
            # make sure to skip itself
            if not(self.UUID==obj.UUID):
                r_12 = obj.pos-self.pos
                distance = np.linalg.norm(r_12)
#                print('distance: ',distance)
                if (distance < (obj.size + self.size)) and not(self.state=='after_bump'):
                    self.state = 'after_bump'
                    obj.state = 'after_bump'
                    self.vel, obj.vel = self.collision_velocity(r_12, self.vel, obj.vel, self.mass, obj.mass)
                    
    
    def collision_velocity(self, r_12, v1, v2, m1, m2):
        # calculate velocities of two colliding objects after collision
        print('Velocities before:',v1,v2)
        print('Velocities before Datatypes:',type(v1),type(v2))

        # junction between v1 and v2
        abs_r_12 = np.linalg.norm(r_12)
        r_12_norm = r_12/abs_r_12
        
        # perpendicular to junction
        r_12_pd = h.perpendicular_norm_vector(r_12)
        r_12_pd = r_12_pd.transpose()
        
        abs_v1 = np.linalg.norm(v1)
        abs_v2 = np.linalg.norm(v2)
        
        # get vector parts of v1 and v2 in direction of r_12 (y) and perpendicular to r_12 (x)
        direction = h.check_direction(v1,r_12_norm)
        print('direction correction v1y ', direction)
        v1_y = np.dot(v1,r_12)/abs_r_12 * r_12_norm
        v1_y = v1_y * direction
        
        direction = h.check_direction(v1,r_12_pd.transpose())
        print('direction correction v1x ', direction)
        v1_x = np.sqrt(abs_v1**2-np.linalg.norm(v1_y)) * r_12_pd
        v1_x = v1_x *direction
        
        direction = h.check_direction(v2,r_12_norm)
        print('direction correction v2y ', direction)
        v2_y = np.dot(v2,r_12)/abs_r_12 * r_12_norm
        v2_y = v2_y * direction
        
        direction = h.check_direction(v2,r_12_pd.transpose())
        print('direction correction v2x ', direction)
        v2_x = np.sqrt(abs_v2**2-np.linalg.norm(v2_y)) * r_12_pd
        v2_x = v2_x * direction
        
        # do 2 elastic collisions one in x and one in y direktion
        v1_new_x =  (m1*v1_x+m2*(2*v2_x-v1_x))/(m1+m2)
        v1_new_y =  (m1*v1_y+m2*(2*v2_y-v1_y))/(m1+m2)        
        
        v2_new_x =  (m2*v2_x+m1*(2*v1_x-v2_x))/(m1+m2)
        v2_new_y =  (m2*v2_y+m1*(2*v1_y-v2_y))/(m1+m2)
        
        # Resulting vector is equal to the vectorial sum of the collision velocites
        # in y and x direction for every individual ball
        v1_new = v1_new_x + v1_new_y
        v2_new = v2_new_x + v2_new_y
        
        print('Velocities after:',np.asanyarray(v1_new),np.asanyarray(v2_new),'\n')    
        print('Velocities after Datatypes:',type(v1_new),type(v2_new),'\n')    
        return np.asanyarray(v1_new),np.asanyarray(v2_new)
    
    def new_pos(self, dt, collec):
        # calculate new position 'self.pos' with current speed 'self.v'
        # after a time increment 'dt' (dtype=float)
        self.collision_check(collec)
#        print(self.pos[1])
        self.pos = self.pos + dt * self.vel
#        print(self.pos[1])


def animate(i):
    # animate next step 
    x, y = [],[]

    for ball in collec:
        ball.new_pos(dt, collec)
        course = ball.pos.transpose()
        
        print('course : ',course)
        print('course : ',course[0])
        print('course Datatype: ', type(course))
        x.append(course[0])
        y.append(course[1])

    l.set_xdata(x)
    l.set_ydata(y)
    return l,


if __name__ == '__main__':
    dt=0.05
    collec = []
    v_1 = np.array([2,-2])
    x_1 = np.array([-4,4])
    ball1 = Ball(4,v_1,x_1)
    collec.append(ball1)
     
    v_2 = np.array([2,2])
    x_2 = np.array([-4,-4])
    ball2 =Ball(3,v_2,x_2)
    collec.append(ball2)
    
    fig, ax = plt.subplots()
    ax.set(xlabel='x (m)', ylabel='y (m)',
       title='collision_simulator')
    ax.set_xlim([-10,10])
    ax.set_ylim([-10,10])
    ax.set_aspect(aspect=1)
    x,y=[],[]
    
    for ball in collec:
        ball.new_pos(dt, collec)
        course = ball.pos
        print('course: ',course)
        x.append(course[0])
        y.append(course[1])
#    l, = ax.plot(x, y, 'o', markersize=25)   
    
    n = 300
    course = np.zeros([n,2,2])
    for m in range(n):
        ball_number = 0
        for ball in collec:
            ball.new_pos(dt,collec)
            course[m,:,ball_number] = ball.pos
            ball_number += 1
#            
    ax.plot(course[:,0,0],course[:,1,0],'r')            
    ax.plot(course[:,0,1],course[:,1,1],'g')
#    ax.plot((course[:,0,1]-course[:,0,0])/2, (course[:,1,1]-course[:,1,0])/2, 'k')
#    ani = animation.FuncAnimation(fig, animate, interval=100)
#        ani.save('fail_01.gif',fps=30)
    plt.show()
       

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        