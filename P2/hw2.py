''' 
Written By: Dong Hyun Lee
Date : 10/23/2018
'''

from doctest import testmod

"""Description: Returns a list that is identical to l but with each value doubled.

    Arguments:
    l -- a list of integers
    """
def doubleAll(l):
    if len (l) == 1:
        return [l[0]*2]
    else:
        return [l[0]*2] + doubleAll(l[1:])
    
    







"""Description: Returns the number of elements in l that are positive.

    Arguments:
    l -- a list of integers
    """
def countPos(l):
    if len (l) == 1:
        if l[0] > 0:
            return len(l[0])
        else:
            return len([])
    else:
        if l[0] > 0:
            return len([l[0]]) + countPos(l[1:])
        else:
            return countPos(l[1:])

        









"""Description: Returns a list of integers in the range low to high, inclusive.
Arguments:
low -- the lower bound (an integer)
high -- the upper bound (an integer) """

def intRange(low, high):
    if [low+1] == [high]:
        return [high]
    else:
        return [low]+intRange(low+1, high)
    











        
"""Description: Merge two sorted integer lists to produce a new sorted list of their elements.

    Arguments:
    l1 -- the first list
    l2 -- the second list
    """
def merge(l1, l2):
    if len(l1)==0:
        return l2[0:]
    if len(l2)==0:
        return l1[0:]
    if l1[0]>l2[0]:
        return [l2[0]] + merge(l1[0:],l2[1:])
    elif l1[0]<=l2[0]:
        return [l1[0]] + merge(l1[1:],l2[0:])
       

# run all doctests whenever this file is run (via the Run menu in IDLE)
if __name__ == '__main__':
    
