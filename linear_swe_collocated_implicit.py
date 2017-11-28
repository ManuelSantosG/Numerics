#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:04:44 2017

@author: ms5717
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import linalg
import OtherFunctions as of
import Experiment as ex

def collocated_implicit(hold,x,dx,c,T=1):
    
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
    
    #circ_vector is the vector that will generate the Toeplitz matrix
    circ_vector=np.zeros(nx)
    circ_vector[0]=1
    circ_vector[2]=0.25*c*c
    circ_vector[nx-2]=-0.25*c*c
    
    
    A=linalg.circulant(circ_vector) #circulant creates a Toeplitz matrix with main row circ_vector
    
    
    p=1
    for i in range(1,nt):
        un=uold.copy()
        b=np.zeros(nx)
        for j in range(1,nx-1):
            b[j]=c*0.5*(hold[j+1]-hold[j-1])
        b[0]=c*0.5*(hold[1]-hold[nx-1])
        b[nx-1]=c*0.5*(hold[0]-hold[nx-2])
        eqb=un-b
        u=np.linalg.solve(A,eqb)
        
    
        
        for j in range(1,nx-1):
            h[j]=hold[j]-0.5*c*(u[j+1]-u[j-1])
        #Boundary values of h
        h[0]=hold[0]-0.5*c*(u[1]-u[nx-1])
        h[nx-1]=hold[nx-1]-0.5*c*(u[0]-u[nx-2])
        
        p+=1
        if p==np.floor(nt/4):
            plt.plot(x, h, label=str(np.round(dt*i,2)))
            plt.plot(x, u, label=str(np.round(dt*i,2)))
            plt.legend()
            #plt.savefig('STuh'+str(dt*i)+'.png')
            plt.show()
            p=1
        
        
        hold=h.copy()
        uold=u.copy()
        
#       L2 error for each timestep
        analytic_h=ex.analytic_sqsin(x,t[i])
        errorh[i]=of.l2ErrorNorm(h,analytic_h)
        
    #    Conservation of mass
        Masst[i]=of.Mass(u,dx)+of.Mass(h,dx)
        
        
    plt.plot(x, h, label='h=1')
    plt.plot(x, u, label='u=1')
    plt.legend()
    plt.show()
    
    plt.plot(t,errorh,label='Error')
    plt.show()
    
    plt.plot(t,Masst,label='Mass')
    plt.show()