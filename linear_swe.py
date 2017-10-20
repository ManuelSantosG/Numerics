#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:30:30 2017

@author: ms5717
"""

import numpy
import math
import matplotlib.pyplot as plt

PPI=math.pi
nt=60
nx=60
x=numpy.linspace(0,2*PPI,nx)
t=numpy.linspace(0,1,nt)

dt=t[1]-t[0]
dx=x[1]-x[0]

c=dt/dx
g=1
H=1
solu=numpy.zeros((nx,nt))
solh=numpy.zeros((nx,nt))


#Initial conditions
#i=0
#while i<nx:
#    solu[i,0]=numpy.sin(x[i])
#    i+=1

#i=0
#while i<nx:
#    solh[i,0]=numpy.sin(x[i])
#    i+=1

#solh[int(nx/2),0]=1


print('Courant number: ', numpy.sqrt(g*H)*0.5*(dt/dx))
i=1
while i<nt:
    j=1
    while j<nx-2:
       solu[j,i]=solu[j,i-1]-0.5*g*c*(solh[j+1,i-1]-solh[j-1,i-1])
       j+=1
       
    j=1
    while j<nx-2:
        if j==nx/2:
           solu[j,i]=solu[j,i-1]-0.5*g*c*(solh[j+1,i-1]-solh[j-1,i-1]) + numpy.sin(8*t[i-1])
        else:
            solu[j,i]=solu[j,i-1]-0.5*g*c*(solh[j+1,i-1]-solh[j-1,i-1])
        solh[j,i]=solh[j,i-1]-0.5*H*c*(solu[j+1,i]-solu[j-1,i])
        j+=1
    
    #Boundary Values
    solu[0,i]=solu[0,i-1]-0.5*c*g*(solh[1,i-1]-solh[nx-2,i-1])
    solh[0,i]=solh[0,i-1]-0.5*c*H*(solu[1,i]-solu[nx-2,i])
    solu[nx-1,i]=solu[0,i]
    solh[nx-1,i]=solh[0,i]
    i+=1

#i=0
#plt.hold(True)
#while i<nt:
#    plt.plot(solh[:,i])
#    i+=1
plt.plot(solh[:,int(nt/2)])