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




#space grid
nx=100

x=numpy.linspace(0,1,nx+1)

dx=1/nx

xmid= 0.5*(x[0:nx] + x[1:nx+1])

c=0.1

T=1
dt=c*dx

#u=numpy.sin(numpy.pi*xmid)**2
u=numpy.zeros(100)
u[25:75]=numpy.ones(50)
uold=u.copy()
plt.plot(xmid,u)
plt.show()
t=dt

p=1
while t<T:
    ub=numpy.zeros(nx+2)
    ub[0]=uold[nx-1]
    ub[nx+1]=uold[0]
    ub[1:nx+1]=uold
    F=0.5*(ub[1:nx+2] + ub[0:nx+1])-0.5*(ub[1:nx+2]-ub[0:nx+1])
    R=F[1:nx+1]-F[0:nx]
    
    u=uold-c*R
    
    uold=u.copy()
    
    plt.plot(xmid,u)
    plt.show()
    
#    p+=1
#    if p==numpy.floor((1/dt)/4):
#        plt.plot(xmid, u,label='u')
#        plt.legend()
#        #plt.savefig('STuh'+str(dt*i)+'.png')
#        plt.show()
#        p=1
    
    t+=dt