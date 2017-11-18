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
h=numpy.zeros(100)
uold=u.copy()
hold=h.copy()
plt.plot(xmid,u)
plt.plot(xmid,h)
plt.show()
t=dt

p=1
while t<T:

    hb=numpy.zeros(nx+2)
    hb[0]=hold[nx-1]
    hb[nx+1]=hold[0]
    hb[1:nx+1]=hold

    
    Fh=0.5*(hb[1:nx+2] + hb[0:nx+1])-0.5*(hb[1:nx+2]-hb[0:nx+1])
    Rh=Fh[1:nx+1]-Fh[0:nx]
    
    u=uold-c*Rh
    uold=u.copy()
    
    ub=numpy.zeros(nx+2)
    ub[0]=uold[nx-1]
    ub[nx+1]=uold[0]
    ub[1:nx+1]=uold
    
    Fu=0.5*(ub[1:nx+2] + ub[0:nx+1])-0.5*(ub[1:nx+2]-ub[0:nx+1])
    Ru=Fu[1:nx+1]-Fu[0:nx]
    
    h=hold-c*Ru
    hold=h.copy()
    
    plt.plot(xmid,u)
    plt.plot(xmid,h)
    plt.show()
    
#    p+=1
#    if p==numpy.floor((1/dt)/4):
#        plt.plot(xmid, u,label='u')
#        plt.legend()
#        #plt.savefig('STuh'+str(dt*i)+'.png')
#        plt.show()
#        p=1
    
    t+=dt