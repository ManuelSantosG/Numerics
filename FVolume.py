#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:42:15 2017

@author: ms5717
"""

import numpy
import math
import matplotlib.pyplot as plt
from scipy import linalg




#space grid and space-step
nx=100
x=numpy.linspace(0,1,nx+1)
dx=1/nx
xmid= 0.5*(x[0:nx] + x[1:nx+1]) #xmid contains the midpoints of the intervales induced by linspace.
                                #The number of elements in xmid is nx



#Courant number
c=0.1


#Time limit and timestep
T=1
dt=c*dx


#Defining initial conditions
n1=math.floor(nx/4)
n2=math.floor(3*nx/4)
h=numpy.zeros(nx)
h[n1:n2] = numpy.sin(2*numpy.pi*(x[n1:n2]-0.25*numpy.ones(n2-n1)))**2
u=numpy.zeros(100)

uold=u.copy()
hold=h.copy()



plt.plot(xmid,u,label='u')
plt.plot(xmid,h,label='h')
plt.legend()
plt.show()


t=dt #Initialise first step

p=1 #This is parameter to get figures, is not relevant for the method

#Core algorithm. Periodic Boundary Conditions
#Loop over all timesteps
while t<T:
    
    #hb is a [nx+2]-length vector that takes into account the periodicity of the grid
    hb=numpy.zeros(nx+2)
    hb[0]=hold[nx-1]
    hb[nx+1]=hold[0]
    hb[1:nx+1]=hold

    
    #Fh is the flux associated to h. It is essentially an upwind scheme adapted to Finite Volumes
    #The length of Fh is nx+1
    Fh=hb[0:nx+1]
    Rh=Fh[1:nx+1]-Fh[0:nx] 
    
    #Update the value of u and save it in uold
    u=uold-c*Rh 
    uold=u.copy()
    
    #Repeat the process for the flux associated to u.
    ub=numpy.zeros(nx+2)
    ub[0]=uold[nx-1]
    ub[nx+1]=uold[0]
    ub[1:nx+1]=uold
    
    
    Fu=ub[0:nx+1]
    Ru=Fu[1:nx+1]-Fu[0:nx]
    
    h=hold-c*Ru
    hold=h.copy()
#    
#    plt.plot(xmid,u)
#    plt.plot(xmid,h)
#    plt.show()
    
    t+=dt
plt.plot(xmid,u)
plt.plot(xmid,h)
plt.show()