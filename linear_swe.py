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
t = numpy.arange(0.,1.,dt)
nt=len(t)


#u = (numpy.sin(numpy.pi*x))**2
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
plt.plot(x, u, label='u0')
plt.legend()
plt.show()


##############
# Core algorithm
##############
p=1
for i in range(0,nt):
    for j in range(1,nx-1):
        u[j]=uold[j]-0.5*c*(hold[j+1] - hold[j-1])
    
    #Boundary values of u
    u[0]=uold[0]-0.5*c*(hold[1] - hold[nx-1])
    u[nx-1]=uold[nx-1]-0.5*c*(hold[0] - hold[nx-2])
    
    for j in range(1,nx-1):
        h[j]=hold[j]-0.5*c*(u[j+1]-u[j-1])
    
    #Boundary values of h
    h[0]=hold[0]-0.5*c*(u[1]-u[nx-1])
    h[nx-1]=hold[nx-1]-0.5*c*(u[0]-u[nx-2])
    
    uold=u.copy()
    hold=h.copy()
    p+=1
    if p==numpy.floor(nx/10):
        plt.plot(x, h, label=str(numpy.round(dt*i,2)))
        plt.plot(x, u, label=str(numpy.round(dt*i,2)))
        plt.legend()
        plt.show()
        p=1
#    if i==math.floor(nt/3): #Plot of the solution half-way to the end
#        plt.plot(x, h, label='h(1/3)')
#        plt.plot(x, u, label='u(1/3)')
#        plt.legend()
#        plt.show()
#    if i==int(nt/2): #Plot of the solution half-way to the end
#        plt.plot(x, h, label='h(1/2)')
#        plt.plot(x, u, label='u(1/2)')
#        plt.legend()
#        plt.show()
#    if i==math.floor(2*nt/3): #Plot of the solution half-way to the end
#        plt.plot(x, h, label='h(2/3)')
#        plt.plot(x, u, label='u(2/3)')
#        plt.legend()
#        plt.show()
        
plt.plot(x, h, label='h(1)')
plt.plot(x, u, label='u(1)')
plt.legend()
plt.show()