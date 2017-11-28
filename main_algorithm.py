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


def maincode(Courant):
    
    ppi=np.pi
    nx=100
    dx = 1./nx
    x = np.arange(0.,1.,dx)
    
    hold=ic.initialcondition(x,3)
    h=hold.copy()
    
    plt.plot(x,h,label='h(x,0)')
    plt.plot(x,np.zeros(nx),label='u(x,0)')
    plt.title('Initial Conditions')
    plt.legend()
    plt.show()
    
    
    co.collocated_explicit(hold,x,dx,Courant,1)
    im.collocated_implicit(hold,x,dx,Courant,1)
    st.staggeredgrid(hold,x,dx,Courant,1)
    
    