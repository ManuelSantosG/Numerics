#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:28:52 2017

@author: ms5717
"""

import numpy as np
import math
import matplotlib.pyplot as plt


ppi=np.pi
nx=10
dx = 1./nx
x = np.arange(0.,1.,dx)
    


def squareWave(x,alpha,beta):
    "A square wave as a function of position, x, which is 1 between alpha"
    "and beta and zero elsewhere. The initialisation is conservative so"
    "that each phi contains the correct quantity integrated over a region"
    "a distance dx/2 either side of x"
    
    phi = np.zeros_like(x)
    
    # The grid spacing (assumed uniform)
    dx = x[1] - x[0]
    
    # Set phi away from the end points (assume zero at the end points)
    for j in range(1,len(x)-1):
        # edges of the grid box (using west and east notation)
        xw = x[j] - 0.5*dx
        xe = x[j] + 0.5*dx
        
        #integral quantity of phi
        phi[j] = max((min(beta, xe) - max(alpha, xw))/dx, 0)

    return phi


def initialcondition(m):
    if m==1:
        hold=squareWave(x,0.45,0.55)
        return hold
    if m==2:
        hold=np.sin(ppi*x)
        return hold
    if m==3:
        hold=(np.sin(ppi*x))**2
        return hold
    if m==4:
        hold=np.zeros(nx)
        n1=math.floor(nx/4)
        n2=math.floor(3*nx/4)
        hold[n1:n2] = np.sin(2*np.pi*(x[n1:n2]-0.25*np.ones(n2-n1)))**2
        return hold



hold=initialcondition(3)
h=hold.copy()


def collocated_explicit(hold,c,T):
    uold=np.zeros(nx)
    u=uold.copy()
    dt=c*dx
    t = np.arange(0.,T,dt)
    nt=len(t)
    
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
        if p==numpy.floor(nt/4):
            plt.plot(x, h, label=str(np.round(dt*i,2)))
            plt.plot(x, u, label=str(np.round(dt*i,2)))
            plt.legend()
            plt.show()
            p=1
            
    plt.plot(x, h, label='h(1)')
    plt.plot(x, u, label='u(1)')
    plt.legend()
    fg=plt.show()
    
    

        
        
        
        
        
        