#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:04:44 2017

@author: ms5717
"""

import numpy
import math
import matplotlib.pyplot as plt
from scipy import linalg


##############
# Global Variables
##############

#space grid
nx=10

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
#h[n1:n2] = numpy.sin(2*numpy.pi*(x[n1:n2]-0.25*numpy.ones(n2-n1)))**2
#h[n1:n2] =numpy.ones(n2-n1)

#h=(numpy.sin(numpy.pi*x))**2
h=numpy.cos(numpy.pi*x)

#h=numpy.zeros(nx)
#h[int(nx/2)]=1
uold = u.copy()
hold = h.copy()


plt.plot(x, h, label='h0')
plt.plot(x, u, label='u0')
plt.legend()
#plt.savefig('STuh0.png')
plt.show()


#circ_vector is the vector that will generate the Toeplitz matrix
circ_vector=numpy.zeros(nx)
circ_vector[0]=1
circ_vector[2]=0.25*c*c*g*H
circ_vector[nx-2]=-0.25*c*c*g*H


A=linalg.circulant(circ_vector) #circulant creates a Toeplitz matrix with main row circ_vector


##############
# Core algorithm, solution for h (only)
##############


p=1
for i in range(1,nt):
    un=uold.copy()
    b=numpy.zeros(nx)
    for j in range(1,nx-1):
        b[j]=c*0.5*(hold[j+1]-hold[j-1])
    b[0]=c*0.5*(hold[1]-hold[nx-1])
    b[nx-1]=c*0.5*(hold[0]-hold[nx-2])
    eqb=un-b
    u=numpy.linalg.solve(A,eqb)
    

    
    for j in range(1,nx-1):
        h[j]=hold[j]-0.5*c*(u[j+1]-u[j-1])
    #Boundary values of h
    h[0]=hold[0]-0.5*c*(u[1]-u[nx-1])
    h[nx-1]=hold[nx-1]-0.5*c*(u[0]-u[nx-2])
    
#    p+=1
#    if p==numpy.floor(nt/4):
#        plt.plot(x, h, label=str(numpy.round(dt*i,2)))
#        plt.plot(x, u, label=str(numpy.round(dt*i,2)))
#        plt.legend()
#        #plt.savefig('STuh'+str(dt*i)+'.png')
#        plt.show()
#        p=1
    
    
    hold=h.copy()
    uold=u.copy()
    
#    plt.plot(x, h, label='h')
#    plt.plot(x, u, label='u')
#    plt.legend()
#    #plt.savefig('STuh0.png')
#    plt.show()
    
    
#plt.plot(x, h, label='h=1')
#plt.plot(x, u, label='u=1')
#plt.legend()
##plt.savefig('STuh0.png')
#plt.show()
    
    
    
    
    
    
    
    
    