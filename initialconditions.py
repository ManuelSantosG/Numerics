#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:33:27 2017

@author: ms5717
"""

import numpy as np

def initialcondition(x,m):
    "This function gives an initial condition discretised function. Depending"
    "on m, the output is different. For m=1, the initial function is a square"
    "wave function. If m=2, the initial condition is a sine function. m=3 gives"
    "a squared sine function. For m=4, the initial condition is the sine bell."
    "For this study, the initial condition for u is taken to be 0 everywhere."
    if m==1:#Squarewave initial condition
        hold=squareWave(x,0.45,0.55)
        return hold
    if m==2:#Sine-profile initial condition
        hold=np.sin(ppi*x)
        return hold
    if m==3:#Square-sine initial condition
        hold=(np.sin(np.pi*x))**2
        return hold
    if m==4: #Sine-bell initial condition
        hold=np.zeros(nx)
        # n1 and n2 are to identify interior points in between which the function will be nonzero.
        n1=math.floor(nx/4)
        n2=math.floor(3*nx/4)
        hold[n1:n2] = np.sin(2*np.pi*(x[n1:n2]-0.25*np.ones(n2-n1)))**2
        return hold