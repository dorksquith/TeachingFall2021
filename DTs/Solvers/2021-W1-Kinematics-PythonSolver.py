import numpy as np

# python script with solutions for M&R workshop 1: kinematics

# Problem 1
print("Problem 1:")
#The position of a particle moving along an x-axis is given by x= 12t^2 − 2t^3, where x is in meters and t is in seconds.  Determine:(a) the position,(b) the velocity, and(c) the acceleration of the particle at t= 4 
# Solution
t = 4
x = 12*pow(t,2) - 2*pow(t,3)
v = 2*12*pow(t,1) - 6*pow(t,2)
a = 2*12*1*pow(t,0) - 6*2*pow(t,1)
print("position at t=4s: %f"%(x))
print("velocity at t=4s: %f"%(v))
print("acceleration at t=4s: %f"%(a))
print("-----")

# Problem 2
print("Problem 2:")
# A rock is thrown vertically upward from ground level at time t= 0.  At t= 1.5 s it passes the top of a talltower, and 1.0 s later it reaches its maximum height.  What is the height of the tower?
# Solution
# 1. What are we explicitly given in the question?
t_tower = 1.5 
t_max = t_tower + 1 
# 2. What do we know that is not explicitly given in the question?
a = -9.81 # acceleration due to gravity
v_max = 0 # velocity at max height (it must momentarily stop)
# 3. We have v,a,t. We want s (at t=1.5). The initial velocity u is unknown.
# v = u + at, so u = v - at
u = v_max - a*t_max
print("u: ",u)
print("a: ",a)

# 4. Now we have uvat
# s = u*t + 0.5*a*pow(t,2) and we want to use t_tower
print("u*t_tower: ",u*t_tower)
print("0.5*a*pow(t_tower,2): ",0.5*a*pow(t_tower,2) )

s_tower = u*t_tower + 0.5*a*pow(t_tower,2)
print("height s_tower: %f"%(s_tower))
print("-----")

# Problem 3
print("Problem 3:")
# Two particles move along an x axis. 
# The position of particle 1 is given by x_1 = 6.00*pow(t,2) + 3.00*t + 2.00;
# the acceleration of particle 2 is given by a_2 = −8.00*t and, at t = 0, its velocity is v_2 = 20 m/s.
# When the velocities of the particles match, what is their velocity?
# Solution
# 1. What are we explicitly given in the question?
# x_1 = 6.00*pow(t,2) + 3.00*t + 2.00
# a_2 = −8.00*t
u_2 = 20
# at some time t, v_2(t) = v_1(t)
# 2. What do we know that is not explicitly given in the question?
# we know how to calculate v_1, by differentiating x_1
# v_1 = 12*pow(t,1) + 3.00
# we know how to calculate v_2, by itegrating a_2
# v_2 = -4*pow(t,2) + c
# we now have v_1 = v_2:
# we find c by sayig when t=0, v_2 = u_2 = 20, so
# v_2 = -4*pow(t,2) + 20

# 12*pow(t,1) + 3.00 = - 4*pow(t,2) + 20
# and we know how to solve a quadratic equation
# 4*pow(t,2) + 12*pow(t,1) - 17 =0
abc = [4, 12, -17] # an array of the coefficients a,b,c of the quadratic
roots = np.roots(abc) # the roots of the array
t = roots[roots>0] # time must be +, so take the positive root
print("positive root t: ",t)
# so finally we plug this value for t back into v_1 (or v_2):
v_1 = 12*pow(t,1) + 3.00
v_2 = 20 - 4*pow(t,2)
print("v_1: %f; v_2: %f "%(v_1,v_2))
print("-----")

# Problem 4
print("Problem 4:")
# A ball is shot vertically upward from the surface of another planet.  A plot of y versus t for the ball is shown inthe figure below, where y is the height of the ball above its starting point and t= 0 at the instant the ball is shot.
# The figure's vertical scaling is set by ys= 30.0m.  What are the magnitudes of :
#(a) the free-fall acceleration on the planet and
#(b) the initial velocity of the ball?
# Solution
# 1. What are we explicitly given in the question/graph?
s_max = 25 # max height
t_max = 2.5 # from the graph
# 2. What do we know that is not explicitly given in the question?
v_max = 0 # velocity at max height (it must momentarily stop)
# we are missing u and a, which are what we must find
# s = v*t - 0.5*a*pow(t,2)
# a = (2/pow(t,2))*(v*t - s)
a = (2/pow(t_max,2))*(v_max*t_max-s_max)
print("acceleration on planet: %f"%(a))
# now find u, using v=u+at
u = v_max - a*t_max
print("initial velocity: %f"%(u))
print("-----")
