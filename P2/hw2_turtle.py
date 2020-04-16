''' 
Written By: Dong Hyun Lee
Date : 10/23/2018
'''

from turtle import *
import time


'''Description: Draws a regular polygon.
    
    Arguments:
    n - the number of sides
    sideLength - the length of each side'''

def regularNGon(n,d):
    helperRegularNGon(n,d,180-180*(n-2)/n)

def helperRegularNGon(n,d, angle):
    if n == 0:
        return
    else: 
        forward(d)
        time.sleep(1)
        left(angle)
        time.sleep(1)
        helperRegularNGon(n-1, d, angle)
        time.sleep(2)










'''Descrpiton: Draws an Archimedean spiral.
    
    Arguments:
    initialLen - the length of the first line segment
    increment - the amount to increment the length for the next segment
    angle - the angle to turn after each segment is drawn
    n - the number of segments to draw'''
def archSpiral(initialLen, increment, angle, n):
    helperArchSpiral(initialLen,increment,angle,n)
def helperArchSpiral(initialLen,increment,angle,n):
    if n==0:
        return
    else:
        forward(initialLen)
        left(angle)
        helperArchSpiral(initialLen+increment,increment,angle,n-1)
        time.sleep(2)
        









'''Descrpiton: Draws an logarithmic spiral.

    Arguments:
    initialLen - the length of the first line segment
    percentIncrease - the percentage to increase the length for the next segment
    angle - the angle to turn after each segment is drawn
    n - the number of segments to draw'''
    
def logSpiral(initialLen, percentIncrease, angle, n):
    helperLogSpiral(initialLen, percentIncrease, angle, n)
def helperLogSpiral(initialLen, percentIncrease, angle, n):
    if n==0:
        return
    else:
        forward(initialLen)
        left(angle)
        helperLogSpiral(initialLen+initialLen*percentIncrease/100,percentIncrease,angle,n-1)
        time.sleep(2)
 
