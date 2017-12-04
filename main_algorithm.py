#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:10:48 2017

@author: ms5717
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import initialconditions as ic
import linear_swe as co
import linear_swe_collocated_implicit as im
import swe_staggered as st
import OtherFunctions as of
import Experiment as ex
import dispersion_relation as drr

#Run this code to get a default output

def maincode(nx,Courant):
    "maincode() runs different methods to solve the Shallow Water Equations"
    "(SWE). This function is fed with a number of nodes, nx, and a Courant number"
    " and creates an initial condition for the problem."
    
    
    dx = 1./nx #Define space-step.
    x = np.arange(0.,1.,dx) #Define space grid.
    
    hold=ic.initialcondition(x,3)
    h=hold.copy()
#    hold=np.zeros(nx)
#    h=hold.copy()
    
    #Plot intial condition
    plt.plot(x,h,label='h(x,0)')
    plt.plot(x,np.zeros(nx),label='u(x,0)')
    plt.title('Initial Conditions')
    plt.legend()
    plt.show()
    
    #Solve SWE using a Collocated Explicit method
    #In the final argument type True to add forcing, False not to add any forcing.
    co.collocated_explicit(hold,x,dx,Courant,1,True)
    
    #Solve SWE using a Collocated Implicit method
    im.collocated_implicit(hold,x,dx,Courant,1)
    
    #Solve SWE using a Staggered-Grid method
    #In the final argument type True to add forcing, False not to add any forcing.
    st.staggeredgrid(hold,x,dx,Courant,1,False)
    
    
#    The following line execute a program that produces the dispersion relations.
    drr.dispersion_relation(Courant)

maincode(100,0.1)