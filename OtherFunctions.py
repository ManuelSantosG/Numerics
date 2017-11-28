#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:26:32 2017

@author: ms5717
"""
import numpy as np
import Experiment as ex

def l2ErrorNorm(phi, phiExact):
    "Calculates the l2 error norm (RMS error) of phi in comparison to"
    "phiExact"
    
    # calculate the error and the RMS error norm
    phiError = phi - phiExact
    l2 = np.sqrt(sum(phiError**2)/sum(phiExact**2))

    return l2


def lInfErrorNorm(phi, phiExact):
    "Calculates the linf error norm (maximum normalised error) in comparison"
    "to phiExact"
    phiError = phi - phiExact
    return np.max(np.abs(phiError))/np.max(np.abs(phiExact))


def Mass(phi,dx):
    "Approximate the integral of some function in a discretised domain of"
    "mesh size dx using a simple quadrature formula"
    nx=len(phi)
    Int=sum(dx*phi)-dx*phi[nx-1]
    return Int
    