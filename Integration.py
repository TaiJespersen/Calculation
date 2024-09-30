#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:51:08 2024

@author: tai
"""
def f(x):
    return x**4 - 2*x + 1


def Trapezoidal(a, b, N):
    h = (b-a)/N
    
    s = 0.5*f(a) + 0.5*f(b)
    for k in range(1,N):
        s += f(a+k*h)
    
    return(h*s)


def Simpsons(a, b, N):
    a = 0.0
    b = 2.0
    h = (b-a)/N
    
    S1 = 0
    for k in range(1,N, 2):
       S1 += f(a + (k * h))
    S1 = S1 * 4
    
    S2 = 0
    for j in range(2, N - 1, 2):
        S2 += f(a + (j * h))
    S2 = S2 * 2
    
    
    return h/3 * (f(a) + f(b) + S1 + S2)

from numpy import ones,copy,cos,tan,pi,linspace



def GaussQuad(a,b, N):
    def gaussxwab(N,a,b):
        def gaussxw(N):
    
            # Initial approximation to roots of the Legendre polynomial
            a = linspace(3,4*N-1,N)/(4*N+2)
            x = cos(pi*a+1/(8*N*N*tan(a)))
    
            # Find roots using Newton's method
            epsilon = 1e-15
            delta = 1.0
            while delta>epsilon:
                p0 = ones(N,float)
                p1 = copy(x)
                for k in range(1,N):
                    p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
                dp = (N+1)*(p0-x*p1)/(1-x*x)
                dx = p1/dp
                x -= dx
                delta = max(abs(dx))
    
            # Calculate the weights
            w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)
    
            return x,w
        x,w = gaussxw(N)
        return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w
    x,w = gaussxwab(N,a,b)
    s = 0.0
    for k in range(N):
        s += w[k]*f(x[k])
    return s