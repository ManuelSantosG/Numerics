#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:45:58 2017

@author: ms5717
"""

import numpy as np

def squareWave(x,t,alpha,beta):
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
        phi[j] = 0.5*max((min(beta, xe-t) - max(alpha, xw-t))/dx, 0) + 0.5*max((min(beta, xe + t) - max(alpha, xw + t))/dx, 0)

    return phi

x=np.linspace(0,1,100)
t=0.2
phi=squareWave(x,t,0.45,0.55)
plt.plot(x,phi)