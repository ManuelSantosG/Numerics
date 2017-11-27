#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:45:41 2017

@author: ms5717
"""
import numpy
import math
import matplotlib.pyplot as plt



def analytic_sqsin(x,t,m):
    for i in range(0,nt):
        hsol=0.5*(numpy.sin(ppi*x - ppi*t[i])**2) + 0.5*(numpy.sin(ppi*x + ppi*t[i])**2)
        usol=0.5*(numpy.sin(ppi*x - ppi*t[i])**2) - 0.5*(numpy.sin(ppi*x + ppi*t[i])**2)
        plt.plot(x,usol,label='u')
        plt.plot(x,hsol,label='h')
        plt.legend()
        plt.show()
    