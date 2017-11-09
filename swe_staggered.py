#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:39:00 2017

@author: ms5717
"""

import numpy
import math
import matplotlib.pyplot as plt
from scipy import linalg

nx=100
x=numpy.arange(0,nx,1)
dx=1/nx
x=dx*x

c=0.1

dt=c*dx

t=numpy.arange(0,100,1)
t=dt*t
nt=len(t)


u=numpy.sin(numpy.sin(numpy.pi*x))
uold=numpy.sin(numpy.sin(numpy.pi*x))


for i in range(1,nt-1):
    for j in range(0,nx-1)
        u[]=uold[j-1]
    
    