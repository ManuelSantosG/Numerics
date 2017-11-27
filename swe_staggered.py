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

def staggeredgrid(hold,c,T=1):
    
    uold=np.zeros(nx)
    u=uold.copy()
    dt=c*dx
    t = np.arange(0.,T,dt)
    nt=len(t)
    
    
    p=1
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
        
        p+=1
        if p==np.floor(nt/4):
            plt.plot(x, h, label='h'+str(np.round(dt*i,2)))
            plt.plot(x, u, label='u'+str(np.round(dt*i,2)))
            plt.legend()
            plt.show()
            p=1
    
    plt.plot(x, h, label='h')
    plt.plot(x, u, label='u')
    plt.legend()
    plt.show()
