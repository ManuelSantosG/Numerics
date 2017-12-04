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

def staggeredgrid(hold,x,dx,c,T,f):
    "Uses a staggeredgrid method to solve the SWE given a discretisation"
    " and a initial condition. It produces 4 snapshots of the solution at certain "
    "times and computes the L2 error with respect to the analytic solution."
    "It also calculates the mass of the approximation to study conservation."
    
    
    nx=len(x)
    uold=np.zeros(nx)# The initial condition for u is taken to be zero everywhere
    u=uold.copy()
    h=hold.copy()
    dt=c*dx # Fix timestep to satisfy stability condition.
    t = np.arange(0.,T,dt)
    nt=len(t)
    
    errorh=np.zeros(nt)#This vector will contain the L2 error of h with respect to the analytic solution at each timestep.
    Masst=np.zeros(nt)#This vector will contain the mass at each timestep.
    
    Masst[0]=of.Mass(hold,dx)
    if f==True:
        p=1#This number will be used to produce plots (see below).
        for i in range(1,nt):
            #We first iterate to compute the new values of u, which depend only on old values of h.
            for j in range(0,nx):
                #u[0] is the value of u_{1/2}^{j} and so on...
                if j==nx-1 or j==int(nx/2):
                    if j==nx-1:
                        u[j]=uold[j]-c*(hold[0]-hold[j])
                    else:
                        u[j]=uold[j]-c*(hold[j+1]-hold[j]) + np.sin(8*t[i])
                else:
                    u[j]=uold[j]-c*(hold[j+1]-hold[j])
                
                    
            for j in range(0,nx): #Since there are no repeated nodes, we apply this formula to obtain the new values of h:
                h[j]=hold[j]-c*(u[j]-u[(j-1)%nx])
                
            
            # Update the old values of u and h.
            uold=u.copy()
            hold=h.copy()
            
            p+=1 #p increases its value until the condition below is satisfied and then the code produces a graph.
            if p==np.floor(nt/4):
                plt.plot(x, c*h, label='u(x,'+str(np.round(dt*i,2))+')')
                plt.plot(x, c*u, label='h(x,'+str(np.round(dt*i,2))+')')
                plt.title('Staggered-Grid Approximation')
                plt.legend()
                plt.show()
                p=1
        
        #   L2 error for each timestep
            analytic_h=ex.analytic_sqsin(x,t[i])
            errorh[i]=of.l2ErrorNorm(h,analytic_h)
            
        #   Conservation of mass   
            Masst[i]=of.Mass(u,dx)+of.Mass(h,dx)
        
    if f==False:
        p=1#This number will be used to produce plots (see below).
        for i in range(1,nt):
            #We first iterate to compute the new values of u, which depend only on old values of h.
            for j in range(0,nx):
                #u[0] is the value of u_{1/2}^{j} and so on...
                if j==nx-1:
                    u[j]=uold[j]-c*(hold[0]-hold[j])
                else:
                    u[j]=uold[j]-c*(hold[j+1]-hold[j])
                
                    
            for j in range(0,nx): #Since there are no repeated nodes, we apply this formula to obtain the new values of h:
                h[j]=hold[j]-c*(u[j]-u[(j-1)%nx])
                
            
            # Update the old values of u and h.
            uold=u.copy()
            hold=h.copy()
            
            p+=1 #p increases its value until the condition below is satisfied and then the code produces a graph.
            if p==np.floor(nt/4):
                plt.plot(x, 0.1*h, label='u(x,'+str(np.round(dt*i,2))+')')
    #            plt.plot(x, 0.1*u, label='h(x,'+str(np.round(dt*i,2))+')')
                plt.title('Staggered-Grid Approximation')
                plt.legend()
                plt.show()
                p=1
        
        #   L2 error for each timestep
            analytic_h=ex.analytic_sqsin(x,t[i])
            errorh[i]=of.l2ErrorNorm(h,analytic_h)
            
        #   Conservation of mass   
            Masst[i]=of.Mass(u,dx)+of.Mass(h,dx)
        
    plt.plot(x, h, label='h(x,1)')
    plt.plot(x, u, label='u(x,1)')
    plt.title('Staggered-Grid Approximation')
    plt.legend()
    plt.show()
    
    plt.plot(t,errorh,label='Error')
    plt.title('c='+str(c))
    plt.show()
    
    plt.plot(t,Masst,label='Mass')
    plt.title(str(nx)+' grid points')
    plt.show()