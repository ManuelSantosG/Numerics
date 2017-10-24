#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:04:44 2017

@author: ms5717
"""

import numpy
import math
import matplotlib.pyplot as plt
from scipy import linalg


##############
# Global Variables
##############

PPI=math.pi
nt=40
nx=10
x=numpy.linspace(0,2*PPI,nx+1)
t=numpy.linspace(0,10,nt)


#Calculate timestep and space-step
dt=t[1]-t[0]
dx=x[1]-x[0]

c=dt/dx #Courant number
g=1
H=1



#The matrices solu and solh store the solutions for u and h
solu=numpy.zeros((nx+1,nt))
solh=numpy.zeros((nx+1,nt))


#Initial Conditions
solh[0:nx,0]=numpy.sin(x[0:nx]/2)



#circ_vector is the vector that will generate the Toeplitz matrix
circ_vector=numpy.zeros(nx)
circ_vector[0]=1
circ_vector[2]=-0.25*c*c*g*H
circ_vector[nx-2]=0.25*c*c*g*H


A=linalg.circulant(circ_vector) #circulant creates a Toeplitz matrix with main row circ_vector


##############
# Core algorithm, solution for h (only)
##############



i=1
while i<nt:
    hn=solh[0:nx,i-1]
    b=numpy.zeros(nx)
    b[0:nx-1]=-0.5*c*H*solu[1:nx,i-1]-0.5*c*H*solu[0:nx-1,i-1]
    b[nx-1]=-0.5*c*H*solu[0,i-1]-0.5*c*H*solu[nx-1,i-1]
    eqb=hn+b
    solh[0:nx,i]=numpy.linalg.solve(A,eqb)
    print('hn: ',hn)
    print('b: ',b)
    print('eqb: ',eqb)
    solh[nx,i]=solh[0,i]
    i+=1


#Uncomment the following to see the sequence of solutions at each timestep    
#i=0
#plt.hold(True)
#while i<nt:
#    plt.plot(solh[:,i])
#    i+=1
    
    
    
    
    
    
    
    
    