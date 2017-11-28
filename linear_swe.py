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
    "Uses a collocated explicit method to solve the SWE given a discretisation"
    " and a initial condition. It produces 4 snapshots of the solution at certain "
    "times and computes the L2 error with respect to the analytic solution."
    "It also calculates the mass of the approximation to study conservation."
    
    nx=len(hold)
    uold=np.zeros(nx)# The initial condition for u is taken to be zero everywhere.
    u=uold.copy()
    h=hold.copy()
    dt=c*dx # Fix timestep to satisfy stability condition.
    t = np.arange(0.,T,dt)
    nt=len(t)
    
    
    errorh=np.zeros(nt)#This vector will contain the L2 error of h with respect to the analytic solution at each timestep.
    Masst=np.zeros(nt) #This vector will contain the mass at each timestep.
    
    p=1 #This number will be used to produce plots (see below).
    for i in range(0,nt):#Iteration of the Collocated Explicit method over timesteps.
        for j in range(1,nx-1):#Iteration over the interior gridpoints to update u.
            u[j]=uold[j]-0.5*c*(hold[j+1] - hold[j-1])
        
        #Boundary values of u
        u[0]=uold[0]-0.5*c*(hold[1] - hold[nx-1])
        u[nx-1]=uold[nx-1]-0.5*c*(hold[0] - hold[nx-2])
        
        for j in range(1,nx-1):#Iteration over the interior gridpoints to update h.
            h[j]=hold[j]-0.5*c*(u[j+1]-u[j-1])
        
        #Boundary values of h
        h[0]=hold[0]-0.5*c*(u[1]-u[nx-1])
        h[nx-1]=hold[nx-1]-0.5*c*(u[0]-u[nx-2])
        
        #Update old values of u and h.
        uold=u.copy()
        hold=h.copy()
        
        
        p+=1 #p increases its value until the condition below is satisfied and then the code produces a graph.
        if p==np.floor(nt/4):
            plt.plot(x, h, label='h(x,'+str(np.round(dt*i,2))+')')
            plt.plot(x, u, label='u(x,'+str(np.round(dt*i,2))+')')
            plt.title('Collocated Explicit method')
            plt.legend()
            plt.show()
            p=1
            
            
        #    L2 error for each timestep
        analytic_h=ex.analytic_sqsin(x,t[i])
        errorh[i]=of.l2ErrorNorm(h,analytic_h)
        
        #    Total mass at each timestep  
        Masst[i]=of.Mass(u,dx)+of.Mass(h,dx)
        
        
    plt.plot(x, h, label='h(x,1)')
    plt.plot(x, u, label='u(x,1)')
    plt.title('Collocated Explicit method')
    plt.legend()
    plt.show()
    
    plt.plot(t,errorh,label='Error')
    plt.title('L2 error of the Collocated Explicit method')
    plt.show()
    
    plt.plot(t,Masst,label='Mass')
    plt.title('Total mass evolution, Collocated Explicit method')
    plt.show()