#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:30:30 2017

@author: ms5717
"""

import numpy
import math
import matplotlib.pyplot as plt

##############
# Global Variables
##############


#space grid
nx=100

dx = 1./nx
x = numpy.arange(0.,1.,dx)
c=0.1 #Courant number
g=1
H=1
dt=c*dx #timestep

#t=numpy.arange(0,10000,10)
t = numpy.arange(0,100,1)
t=dt*t
nt=len(t)

u = numpy.sin(numpy.pi*x)
h = numpy.sin(numpy.pi*x)
uold = u.copy()
hold = h.copy()

plt.plot(x, h, label='h0')
plt.plot(xu, u, label='u0')
plt.legend()
plt.show()


##############
# Core algorithm
##############

for i in range(1,nt):
    for j in range(0,nx):
        if j==0:
            u[0]=uold[0]-0.5*c*(hold[1] - hold[nx-1])
        if j==nx-1:
            u[j]=uold[j]-0.5*c*(hold[0] - hold[j-1])
        else:
            u[j]=uold[j]-0.5*c*(hold[j+1] - hold[j-1])
    for j in range(0,nx):
        if j==0:
            h[0]=hold[0]-0.5*c*(u[1]-u[nx-1])
        if j==nx-1:
            h[j]=hold[j]-0.5*c*(u[0]-u[j-1])
        else:
            h[j]=hold[j]-0.5*c*(u[j+1]-u[j-1])
