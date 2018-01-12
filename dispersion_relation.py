#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:44:45 2017

@author: ms5717
"""
import numpy as np
import matplotlib.pyplot as plt

def dispersion_relation(c):
    
    x=np.linspace(0,3.5,1000)
    
    dx=x[1]-x[0]
    
    drcoex=(2/c)*np.arcsin((c/2)*np.sin(x))
    plt.plot(x,drcoex,label='Collocated Explicit')
    plt.ylabel('Dispersion relation')
    plt.xlabel('Frequency')
    plt.title('c='+str(c))
    plt.grid()
    
    
    drcoim=np.arctan(c*np.sin(x))
    plt.plot(x,drcoim,label='Collocated Implicit')
    
    
    drst=(2/c)*np.arcsin(c*np.sin(0.5*x))
    plt.plot(x,drst,label='Staggered Grid')
    
    
    dran=x
    plt.plot(x,x,label='Analytical')
    
    plt.legend()
    plt.show()
