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
plt.savefig('STuh0.png')
plt.show()




#circ_vector is the vector that will generate the Toeplitz matrix
circ_vector=numpy.zeros(nx)
circ_vector[0]=1
circ_vector[2]=-0.25*c*c*g*H
circ_vector[nx-2]=0.25*c*c*g*H


A=linalg.circulant(circ_vector) #circulant creates a Toeplitz matrix with main row circ_vector


##############
# Core algorithm, solution for h (only)
##############



i=1
while i<nt:
    hn=solh[0:nx,i-1]
    b=numpy.zeros(nx)
    b[0:nx-1]=-0.5*c*H*solu[1:nx,i-1]-0.5*c*H*solu[0:nx-1,i-1]
    b[nx-1]=-0.5*c*H*solu[0,i-1]-0.5*c*H*solu[nx-1,i-1]
    eqb=hn+b
    solh[0:nx,i]=numpy.linalg.solve(A,eqb)
    print('hn: ',hn)
    print('b: ',b)
    print('eqb: ',eqb)
    solh[nx,i]=solh[0,i]
    i+=1


#Uncomment the following to see the sequence of solutions at each timestep    
#i=0
#plt.hold(True)
#while i<nt:
#    plt.plot(solh[:,i])
#    i+=1
    
    
    
    
    
    
    
    
    