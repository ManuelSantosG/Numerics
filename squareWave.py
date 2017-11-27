#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:23:44 2017

@author: ms5717
"""

import numpy as np
import math
import matplotlib.pyplot as plt

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




nx=100
nt=nx
x=numpy.linspace(0,1,nx)
t=numpy.linspace(0,0.5,nt)


for i in range(0,nt):
    hsol=0.5*squareWave(x-t[i],0.4,0.6)+0.5*squareWave(x+t[i],0.4,0.6)
    usol=0.5*squareWave(x-t[i],0.4,0.6)-0.5*squareWave(x+t[i],0.4,0.6)
    plt.plot(x,hsol,label='h')
#    plt.plot(x,usol,label='u')
    plt.legend()
    plt.show()



