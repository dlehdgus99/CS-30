''' 
Written By: Dong Hyun Lee
Date : 11/4/2018
'''



'''Description: A function partition that accepts a value v and a list l and partitions l into a list of elements that are equal to v and a list of all other elements. '''

def partition(v,l):
    if l==[]:
        return [[],[]]
    else:
        if l[0]==v:
            return [[l[0]]+partition(v,l[1:])[0],partition(v,l[1:])[1]]
        else:
            return [partition(v,l[1:])[0],[l[0]]+partition(v,l[1:])[1]]




print(partition(2,[22,3,2,5])



'''Description: A function countDistinct that accepts a list l and returns the number of distinct elements in the list. '''

def countDistinct(l):
    if len(l)==0:
        return len(l)
    else:
        return len([partition(l[0],l)])+countDistinct((partition(l[0],l))[1])
        










'''Description: A function selectionSort that takes a list and returns a list containing the same elements but sorted from least to greatest.'''

def selectionSort(l):
    if l==[]:
        return []
    else:
        return partition(min(l),l)[0]+selectionSort(partition(min(l),l)[1])













'''Description:A function mergeSort that takes a list and returns a list containing the same elements but sorted from least to greatest.'''


# for use in mergesort below; do not edit
def merge(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    elif l1[0] <= l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])


def mergeSort(l):
    if l==[]:
        return []
    else:
        if len(l)==1:
            return [l[0]]
        elif len(l)==2:
            return merge([l[0]],[l[1]])
        elif len(l)%2==0:
            return merge(([merge(merge([l[0]],[l[1]]),merge([l[2]],[l[3]]))]+[mergeSort(l[4:])])[0],(([merge(merge([l[0]],[l[1]]),merge([l[2]],[l[3]]))]+[mergeSort(l[4:])])[1]))
        elif len(l)%2!=0:
            return merge([l[0]],mergeSort(l[1:]))


