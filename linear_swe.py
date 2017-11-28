#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:30:30 2017

@author: ms5717
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import Experiment as ex
import OtherFunctions as of 

def collocated_explicit(hold,x,dx,c,T=1):
    
    
    nx=len(hold)
    uold=np.zeros(nx)
    u=uold.copy()
    h=hold.copy()
    dt=c*dx
    t = np.arange(0.,T,dt)
    nt=len(t)
    
    errorh=np.zeros(nt)
    
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
        if p==np.floor(nt/4):
            plt.plot(x, h, label=str(np.round(dt*i,2)))
            plt.plot(x, u, label=str(np.round(dt*i,2)))
            plt.legend()
            plt.show()
            p=1
            
            
        #    L2 error for each timestep
        analytic_h=ex.analytic_sqsin(x,t[i])
        errorh[i]=of.l2ErrorNorm(h,analytic_h)
        
        
    plt.plot(x, h, label='h(1)')
    plt.plot(x, u, label='u(1)')
    plt.legend()
    plt.show()
    
    plt.plot(t,errorh,label='Error')