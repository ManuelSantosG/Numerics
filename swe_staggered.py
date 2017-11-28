#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:39:00 2017

@author: ms5717
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import linalg
import OtherFunctions as of
import Experiment as ex

def staggeredgrid(hold,x,dx,c,T=1):
    
    nx=len(x)
    uold=np.zeros(nx)
    u=uold.copy()
    h=hold.copy()
    dt=c*dx
    t = np.arange(0.,T,dt)
    nt=len(t)
    
    errorh=np.zeros(nt)
    Masst=np.zeros(nt)
    Masst[0]=of.Mass(hold,dx)
    
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
            plt.plot(x, h, label='h(x,'+str(np.round(dt*i,2))+')')
            plt.plot(x, u, label='u(x,'+str(np.round(dt*i,2))+')')
            plt.legend()
            plt.show()
            p=1
    
#    L2 error for each timestep
        analytic_h=ex.analytic_sqsin(x,t[i])
        errorh[i]=of.l2ErrorNorm(h,analytic_h)
        
    #    Conservation of mass   
        Masst[i]=of.Mass(u,dx)+of.Mass(h,dx)
        
    
    plt.plot(x, h, label='h(x,1)')
    plt.plot(x, u, label='u(x,1)')
    plt.legend()
    plt.show()
    
    plt.plot(t,errorh,label='Error')
    plt.show()
    
    plt.plot(t,Masst,label='Mass')
    plt.show()