''' 
Written By: Dong Hyun Lee
Date : 11/11/2018
'''

from functools import reduce

'''
IMPORTANT:  The only function below that is allowed to use recursion is map2.
All other functions (including any helper functions you write) must not be recursive.  Instead, they should make calls to one or more of map, filter, and reduce to perform the necessary list traversals.
'''

'''
Description: Returns all numbers in the list l that are between lo and hi (inclusive).
>>> inRange(5, 15, [3, 15, 7, 21, 12, 34])
[15, 7, 12]
'''

def inRange(lo, hi, l):
   
    return list(filter(lambda n: n<=hi and n>=lo or n>=hi and n<=lo, l))









'''
Descrpition: Replaces all negative numbers in list l with 0,
leaving all other numbers unchanged.
>>> zeroNegatives([1,3,-4,-6,5,-5])
[1, 3, 0, 0, 5, 0]
'''
def zeroNegatives(l):
    def makeZero(x):
        if x<=0:
            return 0
        else:
            return x
    return list(map(makeZero, l))










'''
Description: Flattens a list of lists into a single list.
>>> flatten([[1,2], [3], [], [4,5,6]])
[1, 2, 3, 4, 5, 6]
'''
def flatten(l):
    return reduce(lambda x,y: x+y,l)













'''
Description: Removes all odd integers from l and divides each even number in half.
The list l is assumed to be a list of integers, and the function returns
a list of integers.
>>> halveEvens([10,21,32,42,55])
[5, 16, 21]
'''
def halveEvens(l):
    return list(map(lambda x:int(x/2), list(filter(lambda x: x%2==0,l))))


















'''    
Description: Behaves like the map function, but it traverses two lists simultaneously.
Specifically, map(f, [x1,...,xn], [y1,...,yn]) returns [f(x1,y1), ..., f(xn,yn)].
You may assume that l1 and l2 have the same length.
>>> map2(lambda x,y: [x,y], [1,2,3], [4,5,6])
[[1, 4], [2, 5], [3, 6]]
'''

def map2(f,l1,l2):
    if len(l1)==0:
        return []
    else:
        return [f(l1[0],l2[0])]+map2(f,l1[1:],l2[1:])
        











'''
Description: Computes the dot product of the vectors v1 and v2, each of which is a list
of numbers.  The dot product of [x1,...,xn] and [y1,...,yn] is
x1*y1 + ... + xn*yn.
You may assume that v1 and v2 have the same length.
NOTE: You will want to make use of the map2 function that you defined above.
>>> dotProduct([1,2,3],[4,5,6])
32    
'''

def dotProduct(v1, v2):

    return reduce(lambda x,y:x+y, (list(map2(lambda x,y:x*y,v1,v2))))
 
