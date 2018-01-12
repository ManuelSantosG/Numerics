#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:45:58 2017

@author: ms5717
"""

import numpy as np

def squareWave(x,t,alpha,beta):
    "This is the function that gives the solution, h, to the SWE where an"
    "initial square wave function has been considered. This is, given the"
    "square function at time 0, squareWave computes the state of the wave at"
    "time t."
    
    phi = np.zeros_like(x)
    
    # The grid spacing (assumed uniform)
    dx = x[1] - x[0]
    
    # Set phi away from the end points (assume zero at the end points)
    for j in range(1,len(x)-1):
        # edges of the grid box (using west and east notation)
        xw = x[j] - 0.5*dx
        xe = x[j] + 0.5*dx
        
        #Analytical form of h
        phi[j] = 0.5*max((min(beta, xe-t) - max(alpha, xw-t))/dx, 0) + 0.5*max((min(beta, xe + t) - max(alpha, xw + t))/dx, 0)

    return phi


