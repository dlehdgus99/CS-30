''' 
Written By: Dong Hyun Lee
Date : 11/27/2018
'''




'''
Description: Returns the number of elements of the list l that are positive.
>>> countPos([1, -4, 0, 4, 8, 0])
3
'''
def countPos(l):
    x=0
    for i in l:
        if i>0:
            x+=1
    return x
print(countPos([1,2,3]))



'''
Description: Computes the dot product of the vectors v1 and v2, each of which is a list
of numbers.  The dot product of [x1,...,xn] and [y1,...,yn] is
x1*y1 + ... + xn*yn. You may assume that v1 and v2 have the same length.
>>> dotProduct([1,2,3],[4,5,6])
32    
'''

def dotProduct(v1, v2):
    x=0
    y=0
    for i in v1:
        x+=i*v2[y]
        y+=1
    return x





'''
Description: Partitions the list l into a list of elements that are equal to the value v
and a list of all other elements. Note that the result of partition should
always be a list that contains exactly two lists.
>>> partition(2, [1,5,3,2,2,1,3,2])
[[2, 2, 2], [1, 5, 3, 1, 3]] 
'''
def partition(v, l):
    x=[]
    y=[]
    for i in l:
        if i==v:
            x+=[i]
        else:
            y+=[i]
    return [x,y]






'''
Description: Converts a given nonnegative integer n to a list of digits.
>>> toDigitList(403)
[4, 0, 3]
'''
def toDigitList(n):
    x=[]
    y=[]
    if n==0:
        return [0]
    while n!=0:
        x+=[n%10]
        n=n//10
        i=len(x)-1
    while i>=0:
        y+=[x[i]]
        i-=1
    return y




'''
Description: function takes a nonnegative integer n and returns a pair of its digital
root and its additive persistence, represented as a list of two numbers.
>>> digitalRootAndPersistence(9879)
[6, 2]
'''

def digitalRootAndPersistence(n):
    a=0
    while n>=10:
        n=sum(toDigitList(n))
        a+=1
    return [n]+[a]




'''
Description: Accepts two integer lists l1 and l2, which are each assumed to be sorted from
least to greatest, and produces a new list that contains the elements of both
lists, also sorted from least to greatest.
'''
def merge(l1, l2):
    i=0
    p=0
    x=[]
    while i<len(l1) and p<len(l2):
        if l1[i]<l2[p]:
            x+=[l1[i]]
            i+=1
        else:
            x+=[l2[p]]
            p+=1
        if i==len(l1):
            x+=l2[p:]
        if p==len(l2):
            x+=l1[i:]
    if l1==[] and l2==[]:
        x+=[]
    if l1==[]:
        x+= l2[0:]
    if l2==[]:
        x+=l1[0:]
    return x

