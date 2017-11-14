#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:45:41 2017

@author: ms5717
"""
import numpy
import math
import matplotlib.pyplot as plt

nx=100
nt=nx
x=numpy.linspace(0,1,nx)
x=numpy.pi*x
t=numpy.linspace(0,1,nt)


for i in range(0,nt):
    h=0.5*numpy.sin(x-t[i]*numpy.ones(nx)) + 0.5*numpy.sin(x+t[i]*numpy.ones(nx))
    u=0.5*numpy.sin(x+t[i]*numpy.ones(nx)) - 0.5*numpy.sin(x-t[i]*numpy.ones(nx))

    plt.plot(x, h, label='h')
    plt.plot(x, u, label='u')
    plt.legend()
    plt.show()