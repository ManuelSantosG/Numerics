#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:39:00 2017

@author: ms5717
"""

import numpy
import math
import matplotlib.pyplot as plt
from scipy import linalg

#space grid
nx=10

dx = 1./nx
x = numpy.arange(0.,1.,dx)
xu= x + 0.5*dx*numpy.ones(len(x))
c=0.1 #Courant number

dt=c*dx #timestep

#t=numpy.arange(0,10000,10)
#t = numpy.arange(0,100,0.5)
#t=dt*t
Tmax=2*numpy.pi
t=numpy.arange(0,Tmax,dt)
nt=len(t)

#initial conditions
u=numpy.zeros(nx)
h=numpy.zeros(nx)
n1=math.floor(nx/4)
n2=math.floor(3*nx/4)
h[n1:n2] = numpy.sin(2*numpy.pi*(x[n1:n2]-0.25*numpy.ones(n2-n1)))**2
#h=numpy.zeros(nx)
#h[int(nx/2)]=1
uold = u.copy()
hold = h.copy()

plt.plot(x, h, label='h0')
plt.plot(xu, u, label='u0')
plt.legend()
plt.show()

#Staggered algorithm, periodic BCs
for i in range(1,nt):
    #We first iterate to compute the new values of u, which depend only on old values of h.
    for j in range(0,nx):
        #u[0] is the value of u_{1/2}^{j} and so on...
        #The only point of conflict is the end of the interval, whose value depends on hold[nx]=hold[0]
        if j==nx-1:
            u[j]=uold[j]-c*(hold[0]-hold[j])
        else:
            u[j]=uold[j]-c*(hold[j+1]-hold[j])
    for j in range(0,nx):
        #The only point of conflict is at the beggining of the interval, whose value depends on u[-1/2]=u[nx-1]
        h[j]=hold[j]-c*(u[j]-u[(j-1)%nx])
    uold=u.copy()
    hold=h.copy()
    
    plt.plot(x, h, label='h')
    plt.plot(x, u, label='u')
    plt.legend()
    plt.show()
