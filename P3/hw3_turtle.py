''' 
Written By: Dong Hyun Lee
Date : 11/4/2018
'''


from turtle import *
import time

'''Description: a function tree that draws a tree.'''

# I've implemented this function for you; do not edit it.
def tree( trunkLength, angle, levels ):
    left(90)
    sidewaysTree(trunkLength, angle, levels)

# This is the function you have to implement.
""" draws a sideways tree
        trunklength = the length of the first line drawn ("the trunk")
        angle = the angle to turn before drawing a branch
        levels = the depth of recursion to which it continues branching
    """
def sidewaysTree( trunkLength, angle, levels ):
    if levels == 0:
        return
    else:
        forward(trunkLength)
        left(angle)
        sidewaysTree(trunkLength/2,angle,levels-1)
        right(angle*2)
        sidewaysTree(trunkLength/2,angle,levels-1)
        left(angle)
        backward(trunkLength)



        



tree(128,30,6)
l=[[3,4],[2,5,1],[1,9,8]]
#want [[30,40],[20,50,10],[10,90,80]]
def innerMultiply(l,n):
    f=lambda x:x*n
    return list(map(lambda innerlist:list(map(f,innerlist)),l))



        
