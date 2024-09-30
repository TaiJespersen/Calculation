#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:33:39 2024

@author: tai
"""

import math

def quadratic(a, b, c):

    def quad1(a, b, c):
            
        x1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        x2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        
        return (x1, x2)
        
    
    def quad2(a, b, c):
    
        x1 = (2 * c) / (-b + math.sqrt((b ** 2) - (4 * a * c)))
        x2 = (2 * c) / (-b - math.sqrt((b ** 2) - (4 * a * c)))
        
        return (x1, x2)
        
    
    if (2 * a) < (-b + math.sqrt((b ** 2) - (4 * a * c))):
        quad2(a, b, c)
    else:
        quad1(a, b, c)
        
        
def cubic(a, b, c, d):
    g = (((-b ** 3)/(27 * a ** 3)) + ((b * c) / (6 * a ** 2)) - d / (2 * a)) 
    h = ((g ** 2) + ((c / (3 * a)) - ((b ** 2) / (9 * a ** 2))) ** 3) ** (1/2)
    C1 = (g + h) ** (1/3)
    C2 = (g - h) ** (1/3)
    
    #Cardano's root
    x1 = C1 + C2 - (b / 3 * a)
    #Roots of Unity to find x2, x3
    ω1 = complex(-0.5, (3) **(1/2) / 2)
    ω2 = complex(-0.5, -(3) ** (1/2) / 2)
    
    x2 = ω1 * C1 + ω2 * C2 - (b / (3 * a))
    x3 = ω2 * C1 + ω1 * C2 - (b / (3 * a))
    
    return (x1, x2, x3)