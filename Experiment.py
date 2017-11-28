#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:45:41 2017

@author: ms5717
"""
import numpy
import math
import matplotlib.pyplot as plt
import ManuelSantos_SWE as ms



def analytic_sqsin(x,t):
    ppi=numpy.pi
    hsol=0.5*(numpy.sin(ppi*x - ppi*t)**2) + 0.5*(numpy.sin(ppi*x + ppi*t)**2)
    usol=0.5*(numpy.sin(ppi*x - ppi*t)**2) - 0.5*(numpy.sin(ppi*x + ppi*t)**2)
#    plt.plot(x,usol,label='u')
#    plt.plot(x,hsol,label='h')
#    plt.legend()
#    plt.show()
    
    return hsol
    

def analytic_sin(x,t):
    hsol=0.5*(numpy.sin(ppi*x - ppi*t)) + 0.5*(numpy.sin(ppi*x + ppi*t))
    usol=0.5*(numpy.sin(ppi*x - ppi*t)) - 0.5*(numpy.sin(ppi*x + ppi*t))
    plt.plot(x,usol,label='u')
    plt.plot(x,hsol,label='h')
    plt.legend()
    plt.show()
