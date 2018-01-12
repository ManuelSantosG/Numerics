#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:45:41 2017

@author: ms5717
"""
import numpy as np
import math
import matplotlib.pyplot as plt



def analytic_sqsin(x,t):
    "This function returns the analytical solution at time t as a function of"
    "the space variable, where the initial condition is a square sine function."
    
    ppi=np.pi
    
    hsol=0.5*(np.sin(ppi*x - ppi*t)**2) + 0.5*(np.sin(ppi*x + ppi*t)**2)
    usol=0.5*(np.sin(ppi*x - ppi*t)**2) - 0.5*(np.sin(ppi*x + ppi*t)**2)
    
    return hsol
    

def analytic_sin(x,t):
    "This function returns the analytical solution at time t as a function of"
    "the space variable, where the initial condition is a sine function."
    
    ppi=numpy.pi
    
    hsol=0.5*(np.sin(ppi*x - ppi*t)) + 0.5*(np.sin(ppi*x + ppi*t))
    usol=0.5*(np.sin(ppi*x - ppi*t)) - 0.5*(np.sin(ppi*x + ppi*t))
    plt.plot(x,usol,label='u')
    plt.plot(x,hsol,label='h')
    plt.legend()
    plt.show()

def sinbell(x,t,dt):
    "This is the function that gives the solution, h, to the SWE where an"
    "initial square wave function has been considered. This is, given the"
    "square function at time 0, squareWave computes the state of the wave at"
    "time t."
    nx=len(x)
    hold=np.zeros(nx)
    hhold=np.zeros(nx)
    hhhold=np.zeros(nx)
    uuuold=np.zeros(nx)
    # n1 and n2 are to identify interior points in between which the function will be nonzero.

    
    i=math.floor(t/dt)
    
    n1=math.floor(nx/4)
    n2=math.floor(3*nx/4)
    new1=(n1-i)%nx
    new2=(n2-i)%nx
    new11=(n1+i)%nx
    new22=(n2+i)%nx
    if new1<new2:
        hold[new1:new2] = np.sin(2*np.pi*(x[n1:n2]-0.25*np.ones(n2-n1)))**2
    else:
        hold[new2:new1] = np.sin(2*np.pi*(x[n1:n2]-0.25*np.ones(n2-n1)))**2
    
    if new11<new22:
        hhold[new11:new22] = np.sin(2*np.pi*(x[n1:n2]-0.25*np.ones(n2-n1)))**2
    else:
        hhold[new22:new11] = np.sin(2*np.pi*(x[n1:n2]-0.25*np.ones(n2-n1)))**2
    
    for j in range(0,nx):
        hhhold[j]=0.5*hold[j]+0.5*hhold[j]
        uuuold[j]=0.5*hold[j]-0.5*hhold[j]
    
    return uuuold

x=np.linspace(0,1,100)
tt=np.linspace(0,1,100)
nt=len(tt)
dt=tt[1]-tt[0]


#t=tt[int(0*25)]
#sol=sinbell(x,t,dt)
#plt.plot(x,sol,label='t=0')

t=tt[int(0)]
sol=sinbell(x,t,dt)
plt.plot(x,sol,label='t=0')


t=tt[int(30)]
sol=sinbell(x,t,dt)
plt.plot(x,sol,label='t=0.3')


t=tt[int(60)]
sol=sinbell(x,t,dt)
plt.plot(x,sol,label='t=0.6')

plt.title('u(x,t)')
plt.legend()
plt.show()





t=tt[int(0*25)]
sol=analytic_sqsin(x,t)
plt.plot(x,sol,label='t=0')

t=tt[int(25)]
sol=analytic_sqsin(x,t)
plt.plot(x,sol,label='t=0.25')

t=tt[int(50)]
sol=analytic_sqsin(x,t)
plt.plot(x,sol,label='t=0.5')

plt.title('h(x,t)')
plt.legend()
plt.show()
