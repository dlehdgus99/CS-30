'''
Description: program that shows how many zeros there are
Written by: Dong Hyun Lee
Date: Dec 9 2018
'''

def minimum(l):
    if len(l)==1:
        return l[0]
    elif l[0]>=l[1]:
        return minimum(l[1:])
    elif l[0]<l[1]:
        return minimum([l[0]]+l[2:])
        
def maximum(l):
    if len(l)==1:
        return l[0]
    elif l[0]<l[1]:
        return maximum(l[1:])
    elif l[0]>=l[1]:
        return maximum([l[0]]+l[2:])


a=int(input('Please enter the size of the list (N): '))
if a>0:
    x=0
    burstList=[]
    while x<a:
        b=int(input('Please enter the number for list (N): '))
        burstList+=[b]
        x+=1
    
    c=0
    
    n=[]
    for i in burstList:
        if i==0:
            c+=1
            n+=[c]
        else:
            c=0
                
    
    
    
    
    def makeListofBurst(n):
        if len(n)>2:
            if n[0]<n[1]:
                return makeListofBurst(n[1:])
            else:
                return [n[0]]+makeListofBurst(n[1:])
        elif len(n)==2:
            if n[0]<n[1]:
                return [n[1]]
            else:
                return [n[0]]+[n[1]]
        elif len(n)==1:
            return [n[0]]
        elif n==[]:
            return []
    
    
    
    
    
    
    
   
    
    
    e=0
    if makeListofBurst(n)==[]:
        print('Results: ')
        print('Burst    Length')
        print('AverageBurstLength:0 ')
        print('minimumBurstLength:0 ')
        print('maximumBurstLength:0 ')
        print('totalNumberOfZeros:0 ')
        
    elif len(makeListofBurst(n))>=1:
        print('Results: ')
        print('Burst    Length')
        for i in makeListofBurst(n):
            print(e+1,'      ',i)
            e+=1
     
        def sumOfNumberOfZeros(n):
            if makeListofBurst(n)==[]:
                return 0
            else:
                return n[0]+sumOfNumberOfZeros(n[1:])
        
        AverageBurstLength=sumOfNumberOfZeros(makeListofBurst(n))/len(makeListofBurst(n))
        minimumBurstLength=minimum(makeListofBurst(n))
        maximumBurstLength=maximum(makeListofBurst(n))
        totalNumberOfZeros=sumOfNumberOfZeros(makeListofBurst(n))
        print('AverageBurstLength: '+str(AverageBurstLength))
        print('minimumBurstLength: '+str(minimumBurstLength))
        print('maximumBurstLength: '+str(maximumBurstLength))
        print('totalNumberOfZeros: '+ str(totalNumberOfZeros))
else:
    print('INVALID INPUT')








k=input('Would you like to exit? Please type YES or NO: ').upper()



while k=='NO':
    a=int(input('Please enter the size of the list (N): '))
    if a>0:
        x=0
        burstList=[]
        while x<a:
            b=int(input('Please enter the number for list (N): '))
            burstList+=[b]
            x+=1
        
        c=0
        
        n=[]
        for i in burstList:
            if i==0:
                c+=1
                n+=[c]
            else:
                c=0
                    

        
    

        
        
        e=0
        if n==[] or makeListofBurst(n)==[]:
            print('Results: ')
            print('Burst    Length')
            print('AverageBurstLength:0 ')
            print('minimumBurstLength:0 ')
            print('maximumBurstLength:0 ')
            print('totalNumberOfZeros:0 ')
        elif len(makeListofBurst(n))>=1:
            print('Results: ')
            print('Burst    Length')
            for i in makeListofBurst(n):
                print(e+1,'     ', i)
                e+=1
         
       
        
            AverageBurstLength=sumOfNumberOfZeros(makeListofBurst(n))/len(makeListofBurst(n))
            minimumBurstLength=minimum(makeListofBurst(n))
            maximumBurstLength=maximum(makeListofBurst(n))
            totalNumberOfZeros=sumOfNumberOfZeros(makeListofBurst(n))
            print('AverageBurstLength: '+str(AverageBurstLength))
            print('minimumBurstLength: '+str(minimumBurstLength))
            print('maximumBurstLength: '+str(maximumBurstLength))
            print('totalNumberOfZeros: '+ str(totalNumberOfZeros))
    else:
        print('INVALID INPUT')
    k=input('Would you like to exit? Please type YES or NO: ').upper()
