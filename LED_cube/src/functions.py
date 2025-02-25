'''
    file to store any and all 3d functions to be able to generate previews as well
    as be able to later convert arrays to an indexable way for when leds become implemented

    functions must adhere to certain guidlines to ensure converting and previewing dont run into any issues

    *NOTE: optional inputs are optional for your implementation function however if you decide not to use them ensure that
    they are defaulted to the value stated in documentaion 
    
    parameters:
        X,Y -   1-d numpy array to be used as the x and y axis of the function
        
        var(optinal) -  a way for the function to change over time such that z=f(x,y,t) where t is a different point in time.
                        this does not necessarily need to be added be if you want to make cool functions that change.
                        NOTE: default value = 0

        mode(optinal) - simple way to define in your function how var acts. this allows you to write a single function while
                        allowing you to make different effects (refer to \animations\(bounce or slide) to see how a function 
                        act in these different "modes")  
                        NOTE: default value = "none"

    returns: an array of equal size of inputs

'''

import numpy as np
from consts import *

def z_func(X, Y, var, mode='none'):
    """
    Default plotted function used by my animated/plotter to show its capabilities
    """
    #l = 7.5 # horizontal shift(where it will be centered around)
    l = np.pi/(points/8)
    k = (np.pi/(points/2))             # period -> T=2*pi/k
    h = points/2
    A = points/2
    if mode == 'bounce':
        A = A*np.cos(var)    # amplitude    
        #A = np.pow(var,1/3)
        #A = np.power(var-8,2)/32-1
        #A = 2.1*np.exp(-np.pow(var-2.5,2)/1.4)-1.06
    else:
        l += var
    #z = cos(A)*sin(kx+l)*sin(ky+l)
    return np.round(A*np.sin(k*X+l)*np.sin(k*Y+l)+h)


def func(X,Y,var,mode="none"):
    """
    function used to test out passing functions into my plotter
    """
    #return (np.power(X-1+var,2)+np.power(Y,2))/10-1
    k = np.pi/112.5
    l = 7.5
    A = (points-2)/2
    return np.round(A*np.cos(np.power(X-l,2)*k+np.power(Y-l,2)*k+var)+A)


def snake(var,mode="parametric"):
    '''
    this function will not follow standard conventions set by this document as it wil
    not be a function of z=f(x,y,t) but rather parametric equations.
    '''
    t = np.linspace(0,points-1,points)

    x = np.sin(t)
    y = np.cos(t)
    z = var*t