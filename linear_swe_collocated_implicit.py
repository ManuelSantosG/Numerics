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
    "Uses a collocated implicit method to solve the SWE given a discretisation"
    " and a initial condition. It produces 4 snapshots of the solution at certain "
    "times and computes the L2 error with respect to the analytic solution."
    "It also calculates the mass of the approximation to study conservation."
        


    nx=len(x)
    uold=np.zeros(nx) # The initial condition for u is taken to be zero everywhere.
    u=uold.copy()
    h=hold.copy()
    dt=c*dx # Fix timestep to satisfy stability condition
    t = np.arange(0.,T,dt)
    nt=len(t)
    
    errorh=np.zeros(nt) #This vector will contain the L2 error of h with respect to the analytic solution at each timestep.
    Masst=np.zeros(nt) #This vector will contain the mass at each timestep.
    
    Masst[0]=of.Mass(hold,dx)
    
    #circ_vector is the vector that will generate the Toeplitz matrix
    circ_vector=np.zeros(nx)
    circ_vector[0]=1
    circ_vector[2]=0.25*c*c
    circ_vector[nx-2]=-0.25*c*c
    
    
    A=linalg.circulant(circ_vector) #circulant creates a Toeplitz matrix with main row circ_vector
    
    
    p=1 #This number will be used to produce plots (see below).
    for i in range(1,nt): #Iteration of the Collocated Implicit method over timesteps.
        un=uold.copy()
        b=np.zeros(nx)#b is the vector that will contain the information of h at the previous timestep.
        #To find the value of b, we iterate over the spacegrid: b_j=0.5*c*(hold_{j+1}-h_{j-1}).
        for j in range(1,nx-1):
            b[j]=c*0.5*(hold[j+1]-hold[j-1])
        b[0]=c*0.5*(hold[1]-hold[nx-1])
        b[nx-1]=c*0.5*(hold[0]-hold[nx-2])
        
        eqb=un-b #eqb contains all the known information, so that the linear sistem is given by Au=eqb.
        u=np.linalg.solve(A,eqb)#Solve the linear system to find u.
        
    
        #Since we know all the updated values of u, we just need to iterate over the spacegrid to find the new values of h.
        for j in range(1,nx-1):
            h[j]=hold[j]-0.5*c*(u[j+1]-u[j-1])
            
        #Boundary values of h
        h[0]=hold[0]-0.5*c*(u[1]-u[nx-1])
        h[nx-1]=hold[nx-1]-0.5*c*(u[0]-u[nx-2])
        
        
        p+=1 #p increases its value until the condition below is satisfied and then the code produces a graph.
        if p==np.floor(nt/4):
            plt.plot(x, h, label='h(x,'+str(np.round(dt*i,2))+')')
            plt.plot(x, u, label='u(x,'+str(np.round(dt*i,2))+')')
            plt.title('Collocated Implicit Approximation')
            plt.legend()
            plt.show()
            p=1
        
        #Update old values of u and h.
        hold=h.copy()
        uold=u.copy()
        
#       L2 error for each timestep
        analytic_h=ex.analytic_sqsin(x,t[i])
        errorh[i]=of.l2ErrorNorm(h,analytic_h)
        
#       Total mass at each timestep
        Masst[i]=of.Mass(u,dx)+of.Mass(h,dx)
        
    
    plt.plot(x, h, label='h(x,1)')
    plt.plot(x, u, label='u(x,1)')
    plt.title('Collocated Implicit method')
    plt.legend()
    plt.show()
    
    plt.plot(t,errorh,label='Error')
    plt.title('L2 error of the Collocated Implicit method')
    plt.show()
    
    plt.plot(t,Masst,label='Mass')
    plt.title('Total mass evolution, Collocated Implicit method')
    plt.show()